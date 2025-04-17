import json
import re

def convert_data(input_file, output_file):
    with open(input_file) as f:
        data = [json.loads(line) for line in f]
    
    formatted = []
    for item in data:
        numbers = [float(x) for x in re.findall(r'\d+', item["Problem"])]
        formatted.append({
            "problem": item["Problem"],
            "numbers": numbers,
            "formula": item["annotated_formula"],
            "answer": re.findall(r'\d+', item["correct"])[0]
        })
    
    with open(output_file, 'w') as f:
        json.dump(formatted, f)

convert_data('data/math/challenge_test.json', 'data/math/train_data.json')