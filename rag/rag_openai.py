from langchain_google_genai import GoogleGenerativeAI
from trulens.providers.langchain import Langchain

llm = GoogleGenerativeAI(model="gemini-pro")
langchain_provider = Langchain(chain = llm)


from trulens.core import Feedback
from trulens.feedback import GroundTruthAgreement

golden_set = [
    {"query": "who invented the lightbulb?", "expected_response": "Thomas Edison"},
    {"query": "¿quien invento la bombilla?", "expected_response": "Thomas Edison"}
]
ground_truth_collection = GroundTruthAgreement(golden_set, provider=llm())

feedback = Feedback(ground_truth_collection.agreement_measure).on_input_output()