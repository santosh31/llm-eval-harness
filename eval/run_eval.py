import json
from metrics import exact_match,token_f1

with open("datasets/dataset.json") as f:
    dataset = json.load(f)

for case in dataset:
    em =exact_match(case["output"],case["reference"])
    f1 = token_f1(case["output"],case["reference"])
    print(f'{case["id"]:>2} | EM: {str(em):5} | F1: {f1:.2f} | {case["output"][:45]}')