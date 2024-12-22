import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    """
    Convert a CSV file with Question and Answer columns to a JSON file.
    
    Parameters:
    csv_file_path (str): Path to the input CSV file
    json_file_path (str): Path where the JSON file will be saved
    
    Returns:
    list: The list of question-answer pairs that was written to the JSON file
    """
    qa_pairs = []
    
    # Read the CSV file
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Convert each row to a dictionary
        for row in csv_reader:
            qa_pair = {
                "question": row["Question"].strip(),
                "answer": row["Ground Truth"].strip()
            }
            qa_pairs.append(qa_pair)
    
    # Write to JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(qa_pairs, json_file, indent=2, ensure_ascii=False)
    
    return qa_pairs


# Example usage
csv_file = "MOHAP Questions - COT - COT Questions.csv"
json_file = "output.json"

result = csv_to_json(csv_file, json_file)