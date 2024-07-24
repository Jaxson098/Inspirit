# from transformers import pipeline

# classifier = pipeline("zero-shot-classification")
# labels=["millitary spending","defense"]
# result = classifier("I think we are spending to juch on defense", labels)
# print("l;kasjdf")
# print(result["labels"][0])

# import pandas as pd

# electorateData_vote = pd.read_csv("/home/jaxson/Inspirit/data/electionResults.csv")
# print(electorateData_vote)

import csv

# with open('/home/jaxson/Inspirit/data/abortion.csv', mode='r') as file:
#     reader = csv.reader(file)
    
#     for row in reader:
#         if 'year' in row[0]:  # Adjust the index based on your CSV structure
#             print(row)

# with open('/home/jaxson/Inspirit/data/abortion.csv', mode='r') as file:
#     reader = csv.reader(file)
#     rows = []
            
#     for row in reader:
#         if '2009' in row[0]:  # Adjust the index based on your CSV structure
#             rows.append(row)
# abortionPoll = rows[-1]
# print(abortionPoll)
def getPollData(self, path):
    with open(path, mode='r') as file:
        reader = csv.reader(file)
        rows = []

        for row in reader:
            if '2012' in row[0]:  # Adjust the index based on your CSV structure
                rows.append(row)
    return rows[-1]
class Test:
    def __init__(self):  # Constructor method
        pass

    # Call the getPollData method with the specified path
        abortionPoll = getPollData('/home/jaxson/Inspirit/data/abortion.csv')

        # Print the result
        print(abortionPoll)


# class Test:
#     def getPollData(self, path):
#         with open(path, mode='r') as file:
#             reader = csv.reader(file)
#             rows = []
                
#             for row in reader:
#                 if '2012' in row[0]:  # Adjust the index based on your CSV structure
#                     rows.append(row)
#         return rows[-1]

# className = Test()
# abortionPoll = className.getPollData(path= '/home/jaxson/Inspirit/data/abortion.csv')
# print(abortionPoll)