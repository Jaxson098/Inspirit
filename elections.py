import pandas
import csv

class Election:
    def __init__(self, election_year, election_cantidates):
        year = election_year
        cantidates = election_cantidates

        with open('/home/jaxson/Inspirit/data/abortion.csv', mode='r') as file:
            reader = csv.reader(file)
            
            for row in reader:
                if year in row[0]:  # Adjust the index based on your CSV structure
                    print(row)
                    break