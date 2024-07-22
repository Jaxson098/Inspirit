from transformers import pipeline

classifier = pipeline("zero-shot-classification")
labels=["millitary spending","defense"]
result = classifier("I think we are spending to juch on defense", labels)
print("l;kasjdf")
print(result["labels"][0])