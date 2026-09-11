import re
from collections import Counter

# below function is used to remove the all puncutation mark and special character and return only series of characters and number in original order
def normalize(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]','',text)
    return re.sub(r'\s+',' ',text)

def exact_match(prediction:str,reference:str)->bool:
    return normalize(prediction)==normalize(reference)

#One similarity metric (token F1, no dependencies)
def token_f1(prediction:str, reference:str)-> float:
    pred = normalize(prediction).split()
    ref = normalize(reference).split()
    if not pred and not ref :
        return 0.0
    common = Counter(pred) & Counter(ref)
    same = sum(common.values())
    if same == 0 :
        return 0.0
    precision = same/len(pred)
    recall = same/len(ref)
    return 2*precision*recall/(precision+recall) 