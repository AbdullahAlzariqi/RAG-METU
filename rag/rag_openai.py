
from openai import OpenAI
from trulens.apps.custom import instrument
from trulens.core import TruSession

oai_client = OpenAI()


class rag_openai:
    @instrument
    def retrieve(self, query: str) -> list:
        """
        Retrieve relevant text from vector store.
        """
        results = vector_store.query(query_texts=query, n_results=4)
        # Flatten the list of lists into a single list
        return [doc for sublist in results["documents"] for doc in sublist]

    @instrument
    def generate_completion(self, query: str, context_str: list) -> str:
        """
        Generate answer from context.
        """
        if len(context_str) == 0:
            return "Sorry, I couldn't find an answer to your question."

        completion = (
            oai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                temperature=0,
                messages=[
                    {
                        "role": "user",
                        "content": f"We have provided context information below. \n"
                        f"---------------------\n"
                        f"{context_str}"
                        f"\n---------------------\n"
                        f"First, say hello and that you're happy to help. \n"
                        f"\n---------------------\n"
                        f"Then, given this information, please answer the question: {query}",
                    }
                ],
            )
            .choices[0]
            .message.content
        )
        if completion:
            return completion
        else:
            return "Did not find an answer."

    @instrument
    def query(self, query: str) -> str:
        context_str = self.retrieve(query=query)
        completion = self.generate_completion(
            query=query, context_str=context_str
        )
        return completion


rag = RAG()