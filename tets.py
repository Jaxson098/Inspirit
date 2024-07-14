from transformers import pipeline

classifier = pipeline("zero-shot-classification")
labels=["healthcare", "crime"]
result = classifier("I think healthcare is good", labels)
print("l;kasjdf")
print(result["labels"][0])