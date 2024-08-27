import csv

# Create a sample list of values
data = ['10', 'a', 'b', 'c', 'd']

# Open the file in write mode
with open('./testcsv.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    
    writer.writerow(data)


# name = {'name': 'john', 'name2': 'bill'}
# str(name)
# age = "30"
# country = "USA"

# data = {'Name': name, 'Age': age, 'Country': country}
# df = pd.DataFrame([data])
# df.to_csv('output.csv', index=False, header=False)


# classifier = pipeline("zero-shot-classification")
# labels=["millitary spending","defense"]
# result = classifier("I think we are spending to juch on defense", labels)
# print("l;kasjdf")
# print(result["labels"][0])

# import pandas as pd

# electorateData_vote = pd.read_csv("/home/jaxson/Inspirit/data/electionResults.csv")
# print(electorateData_vote)

# import csv

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
# def getPollData(self, path):
#     with open(path, mode='r') as file:
#         reader = csv.reader(file)
#         rows = []

#         for row in reader:
#             if '2012' in row[0]:  # Adjust the index based on your CSV structure
#                 rows.append(row)
#     return rows[-1]
# class Test:
#     def __init__(self):  # Constructor method
#         pass

#     # Call the getPollData method with the specified path
#         abortionPoll = getPollData('/home/jaxson/Inspirit/data/abortion.csv')

#         # Print the result
#         print(abortionPoll)


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
# import pandas as pd

# # Example dictionaries
# dict1 = {'type': 1, 'name': 'John', 'surname': 'Doe', 'phone': '555-1234'}
# dict2 = {'type': 2, 'name': 'harry', 'surname': 'joe', 'phone': '555-1234'}

# # Flatten the dictionaries
# flattened_dict = {**dict1, **dict2}

# # Create a DataFrame from the flattened dictionary
# df = pd.DataFrame([flattened_dict])

# print(df)
