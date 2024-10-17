import csv
from hugchat import hugchat
from hugchat.login import Login
from collections import Counter
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import requests
import json
import regex as re


abortion_catagories = ["Abortion should always Legal", "Abortion should be sometimes legal", "Abortion should be illegal", "no opinion about abortion"]
crime_catagories = ["satisfied with crime","dissatisfied with crime","No opinion about crime"]
millitarySpending_catagories = ["Too little Millitary spending", "Too much Millitary spending", "no opinion about Millitary spending"]
education_catagories = ["very satisfied with education","Somewhat satisfied with Education","Somewhat dissatisfied with Education","Completely dissatisfied with Education","No opinion about Education"]
guns_catagories = ["More strict gun restrictions","Less strict gun restrictions","gun restrictions Kept as now","No opinion about gun restrictions"]
healthcare_catagories = ["healthcare is governments responsibility","healthcare is not governments responsibility", "no opinion about healthcare"]
imagration_catagories = ["imagration should be kept at Present level","imagration should be Increased","imagration should be Decreased","No opinion about imagration"]
defense_catagories = ["national security Stronger than needs to be","national security Not strong enough","national security About right","no opinion about national security"]

url = "http://localhost:11434/api/chat"

def llama3(prompt):
    data = {
        "model": "llama3.1",
        "messages": [
            {
              "role": "user",
              "content": prompt
            }
        ],
        "stream": False
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    return(response.json()['message']['content'])

def get_poll_percentage(path, year):
    with open(path, mode='r') as file:
        reader = csv.reader(file)
        rows = []
        int_row = []
            
        for row in reader:
            if str(year) in row[0]: 
                rows.append(row)

    yearData = rows[-1]
    
    for i in yearData:
        int_row.append(int(i))

    maxValue = max(int_row)
    return maxValue

def get_poll_index(path, year):
    with open(path, mode='r') as file:
        reader = csv.reader(file)
        rows = []
        int_row = []
            
        for row in reader:
            if str(year) in row[0]: 
                rows.append(row)

                
    yearData = rows[-1]

    for i in yearData:
        int_row.append(int(i))

    maxValue = max(int_row)
    labelIndex = int_row.index(maxValue) -1
    return labelIndex

class cantidate:
    def __init__(self,cantidate_name):

        # abortion_catagories = ["'Abortion should always be Legal'", "'Abortion should be sometimes legal'", "'Abortion should be illegal'", "'no opinion about abortion'"]
        # crime_catagories = ["'satisfied with crime'","'dissatisfied with crime'","'No opinion about crime'"]
        # millitarySpending_catagories = ["'Too little Millitary spending'", "'Too much Millitary spending'", "'no opinion about Millitary spending'"]
        # education_catagories = ["'very satisfied with education'","'Somewhat satisfied with Education'","'Somewhat dissatisfied with Education'","'Completely dissatisfied with Education'","'No opinion about Education'"]
        # guns_catagories = ["'More strict gun restrictions'","'Less strict gun restrictions'","'gun restrictions Kept as now'","'No opinion about gun restrictions'"]
        # healthcare_catagories = ["'healthcare is governments responsibility'","'healthcare is not governments responsibility'", "'no opinion about healthcare'"]
        # imagration_catagories = ["'imagration should be kept at Present level'","'imagration should be Increased'","'imagration should be Decreased'","'No opinion about imagration'"]
        # defense_catagories = ["'national security Stronger than needs to be'","'national security Not strong enough'","'national security About right'","'no opinion about national security'"]

        abortion_catagories = ["abortion should always be legal", "abortion should be sometimes legal", "abortion should be illegal", "no opinion about abortion"]
        crime_catagories = ["satisfied with crime","dissatisfied with crime","no opinion about crime"]
        millitarySpending_catagories = ["too little military spending", "too much millitary spending", "no opinion about millitary spending"]
        education_catagories = ["very satisfied with education","somewhat satisfied with education","somewhat dissatisfied with education","completely dissatisfied with education","no opinion about education"]
        guns_catagories = ["more strict gun restrictions","less strict gun restrictions","gun restrictions kept as now","no opinion about gun restrictions"]
        healthcare_catagories = ["healthcare is governments responsibility","healthcare is not governments responsibility", "'no opinion about healthcare'"]
        imagration_catagories = ["imagration should be kept at present level","imagration should be increased","imagration should be decreased","no opinion about imagration"]
        defense_catagories = ["national security stronger than needs to be","national security not strong enough","national security about right","no opinion about national security"]

        # abortion_txt = f'/Users/jaxsonpaige/Inspirit/rawText/{cantidate_name}/abortion.txt'
        # crime_txt = f'/Users/jaxsonpaige/Inspirit/rawText/{cantidate_name}/crime.txt'
        # defense_spending_txt = f'/Users/jaxsonpaige/Inspirit/rawText/{cantidate_name}/defense spending.txt'
        # education_txt = f'/Users/jaxsonpaige/Inspirit/rawText/{cantidate_name}/education.txt'
        # gun_violence_txt = f'/Users/jaxsonpaige/Inspirit/rawText/{cantidate_name}/gun violence.txt'
        # healthcare_txt = f'/Users/jaxsonpaige/Inspirit/rawText/{cantidate_name}/healthcare.txt'
        # immigration_txt = f'/Users/jaxsonpaige/Inspirit/rawText/{cantidate_name}/immigration.txt'
        # national_security_txt = f'/Users/jaxsonpaige/Inspirit/rawText/{cantidate_name}/national security.txt'

        abortion_txt = f'/home/jaxson/Inspirit/rawText/{cantidate_name}/abortion.txt'
        crime_txt = f'/home/jaxson/Inspirit/rawText/{cantidate_name}/crime.txt'
        defense_spending_txt = f'/home/jaxson/Inspirit/rawText/{cantidate_name}/defense spending.txt'
        education_txt = f'/home/jaxson/Inspirit/rawText/{cantidate_name}/education.txt'
        gun_violence_txt = f'/home/jaxson/Inspirit/rawText/{cantidate_name}/gun violence.txt'
        healthcare_txt = f'/home/jaxson/Inspirit/rawText/{cantidate_name}/healthcare.txt'
        immigration_txt = f'/home/jaxson/Inspirit/rawText/{cantidate_name}/immigration.txt'
        national_security_txt = f'/home/jaxson/Inspirit/rawText/{cantidate_name}/national security.txt'

        abortion_labels = []
        crime_labels = []
        defense_spending_labels = []
        education_labels = []
        gun_violence_labels = []
        healthcare_labels = []
        immigration_labels = []
        national_security_labels = []

        def scoring(path,catagories,label_list):
            with open(path, "r") as file:
                for line in file:
                    score = llama3(f"do not answer with anything but one of these categories with no punctuation: {catagories}. which of those categories do you thin fits this sentence best: {line}")
                    noPunc = re.sub(r"[\'\"\.\[\]]", "", str(score))
                    label_list.append(noPunc.lower())
                    print(f"line: {line}")
                    print(f"score: {noPunc.lower()}\n")

        scoring(abortion_txt,abortion_catagories,abortion_labels)
        s    yearData = rows[-1]coring(crime_txt,crime_catagories,crime_labels)
        scoring(defense_spending_txt,millitarySpending_catagories,defense_spending_labels)
        scoring(education_txt,education_catagories,education_labels)
        scoring(gun_violence_txt,guns_catagories,gun_violence_labels)
        scoring(healthcare_txt,healthcare_catagories,healthcare_labels)
        scoring(immigration_txt,imagration_catagories,immigration_labels)
        scoring(national_security_txt,defense_catagories,national_security_labels)

        abortion_counted = Counter(abortion_labels)
        crime_counted = Counter(crime_labels)
        defense_spending_counted = Counter(defense_spending_labels)
        education_counted = Counter(education_labels)
        gun_violence_counted = Counter(gun_violence_labels)
        healthcare_counted = Counter(healthcare_labels)
        immigration_counted = Counter(immigration_labels)
        national_security_counted = Counter(national_security_labels)

        print(f"\nabortion_counted:{str(abortion_counted.most_common()[0][0])}")
        print(f"\ncrime_counted: {str(crime_counted.most_common()[0][0])}")
        print(f"\ndefense_spending_counted: {str(defense_spending_counted.most_common()[0][0])}")
        print(f"\neducation_counted: {str(education_counted.most_common()[0][0])}")
        print(f"\ngun_violence_counted: {str(gun_violence_counted.most_common()[0][0])}")
        print(f"\nhealthcare_counted: {str(healthcare_counted.most_common()[0][0])}")
        print(f"\nimmigration_counted: {str(immigration_counted.most_common()[0][0])}")
        print(f"\nnational_security_counted: {str(national_security_counted.most_common()[0][0])}")

        self.abortion_index = abortion_catagories.index(str(abortion_counted.most_common()[0][0]))
        self.crime_index = crime_catagories.index(str(crime_counted.most_common()[0][0]))
        self.defense_spending_index = millitarySpending_catagories.index(str(defense_spending_counted.most_common()[0][0]))
        self.education_index = education_catagories.index(str(education_counted.most_common()[0][0]))
        self.gun_violence_index = guns_catagories.index(str(gun_violence_counted.most_common()[0][0]))
        self.healthcare_index = healthcare_catagories.index(str(healthcare_counted.most_common()[0][0]))
        self.immigration_index = imagration_catagories.index(str(immigration_counted.most_common()[0][0]))
        self.national_security_index = defense_catagories.index(str(national_security_counted.most_common()[0][0]))


class Election:
    def __init__(self, election_year, cantidate_1, cantidate_2):

        abortion_poll_percentage = get_poll_percentage('/home/jaxson/Inspirit/data/abortion.csv', year=election_year)
        crime_poll_percentage = get_poll_percentage('/home/jaxson/Inspirit/data/crimePolicies.csv', year=election_year)
        millitarySpending_poll_percentage = get_poll_percentage('/home/jaxson/Inspirit/data/defenseSpending.csv', year=election_year)
        education_poll_percentage = get_poll_percentage('/home/jaxson/Inspirit/data/education.csv', year=election_year)
        guns_poll_percentage = get_poll_percentage('/home/jaxson/Inspirit/data/guns.csv', year=election_year)
        healthcare_poll_percentage = get_poll_percentage('/home/jaxson/Inspirit/data/healthcare.csv', year=election_year)
        imagration_poll_percentage = get_poll_percentage('/home/jaxson/Inspirit/data/imagration.csv', year=election_year)
        defense_poll_percentage = get_poll_percentage('/home/jaxson/Inspirit/data/nationalSecurity.csv', year=election_year)

        abortion_poll_index = get_poll_index('/home/jaxson/Inspirit/data/abortion.csv', year=election_year)
        crime_poll_index = get_poll_index('/home/jaxson/Inspirit/data/crimePolicies.csv', year=election_year)
        millitarySpending_poll_index = get_poll_index('/home/jaxson/Inspirit/data/defenseSpending.csv', year=election_year)
        education_poll_index = get_poll_index('/home/jaxson/Inspirit/data/education.csv', year=election_year)
        guns_poll_index = get_poll_index('/home/jaxson/Inspirit/data/guns.csv', year=election_year)
        healthcare_poll_index = get_poll_index('/home/jaxson/Inspirit/data/healthcare.csv', year=election_year)
        imagration_poll_index = get_poll_index('/home/jaxson/Inspirit/data/imagration.csv', year=election_year)
        defense_poll_index = get_poll_index('/home/jaxson/Inspirit/data/nationalSecurity.csv', year=election_year)

        # can1_Abortion_percentage = abortion_catagories.index(cantidate_1.abortion_scores["scores"][0])
        # can1_Crime_percentage = crime_catagories.index(cantidate_1.crime_scores["scores"][0])
        # can1_MillitarySpending_percentage = millitarySpending_catagories.index(cantidate_1.millitarySpending_scores["scores"][0])
        # can1_Education_percentage = education_catagories.index(cantidate_1.education_scores["scores"][0])
        # can1_Guns_percentage = guns_catagories.index(cantidate_1.guns_scores["scores"][0])
        # can1_Healthcare_percentage = healthcare_catagories.index(cantidate_1.healthcare_scores["scores"][0])
        # can1_Imagration_percentage = imagration_catagories.index(cantidate_1.imagration_scores["scores"][0])
        # can1_Defense_percentage = defense_catagories.index(cantidate_1.defense_scores["scores"][0])

        can1_Abortion_index = cantidate_1.abortion_index
        print(f"\ncan1 abortion index: {can1_Abortion_index}\n")
        can1_Crime_index = cantidate_1.crime_index
        can1_MillitarySpending_index = cantidate_1.defense_spending_index
        can1_Education_index = cantidate_1.education_index
        can1_Guns_index = cantidate_1.gun_violence_index
        can1_Healthcare_index = cantidate_1.healthcare_index
        can1_Imagration_index = cantidate_1.immigration_index
        can1_Defense_index = cantidate_1.national_security_index

        # can2_Abortion_percentage = abortion_catagories.index(cantidate_2.abortion_scores["scores"][0])
        # can2_Crime_percentage = crime_catagories.index(cantidate_2.crime_scores["scores"][0])
        # can2_MillitarySpending_percentage = millitarySpending_catagories.index(cantidate_2.millitarySpending_scores["scores"][0])
        # can2_Education_percentage = education_catagories.index(cantidate_2.education_scores["scores"][0])
        # can2_Guns_percentage = guns_catagories.index(cantidate_2.guns_scores["scores"][0])
        # can2_Healthcare_percentage = healthcare_catagories.index(cantidate_2.healthcare_scores["scores"][0])
        # can2_Imagration_percentage = imagration_catagories.index(cantidate_2.imagration_scores["scores"][0])
        # can2_Defense_percentage = defense_catagories.index(cantidate_2.defense_scores["scores"][0])

        can2_Abortion_index = cantidate_2.abortion_index
        can2_Crime_index = cantidate_2.abortion_index
        can2_MillitarySpending_index = cantidate_2.abortion_index
        can2_Education_index = cantidate_2.abortion_index
        can2_Guns_index = cantidate_2.abortion_index
        can2_Healthcare_index = cantidate_2.abortion_index
        can2_Imagration_index = cantidate_2.abortion_index
        can2_Defense_index = cantidate_2.abortion_index

        data = [can1_Abortion_index,can2_Abortion_index,abortion_poll_percentage,abortion_poll_index,
                can1_Crime_index,can2_Crime_index,crime_poll_percentage,crime_poll_index,
                can1_MillitarySpending_index,can2_MillitarySpending_index,millitarySpending_poll_percentage,millitarySpending_poll_index,
                can1_Education_index,can2_Education_index,education_poll_percentage,education_poll_index,
                can1_Guns_index,can2_Guns_index,guns_poll_percentage,guns_poll_index,
                can1_Healthcare_index,can2_Healthcare_index,healthcare_poll_percentage,healthcare_poll_index,
                can1_Imagration_index,can2_Imagration_index,imagration_poll_percentage,imagration_poll_index,
                can1_Defense_index,can2_Defense_index,defense_poll_percentage,defense_poll_index
                ]
        
        with open(f'./{election_year}.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)

# biden = cantidate("biden")
# trump = cantidate("trump")
# obama = cantidate("obama")
# reagen = cantidate("reagen")

# Wbush = cantidate("Wbush")

# HWbush = cantidate("HWbush")

# # dukakis = cantidate("dukakis")
# # kerry = cantidate("kerry")

clinton = cantidate("clinton")
# Hclinton = cantidate("Hclinton")
# carter = cantidate("carter")
dole = cantidate("dole")

# # gore = cantidate("gore")

# mccain = cantidate("mccain")
# romney = cantidate("romney")

# mondle = cantidate("mondle")
# kenedy = cantidate("kenedy")
# nixon = cantidate("nixon")
# ford = cantidate("ford")
# perot = cantidate("perot")

# Election(2020,biden,trump)
# Election(2016,Hclinton,trump)
# Election(2012,obama,romney)
# Election(2008,obama,mccain)
Election(1996,clinton,dole)
# Election(1992,clinton,HWbush)
# Election(1980,carter,reagen)

# Election(2004,kerry,Wbush)
# Election(2000,gore,Wbush)

# Election(1988,dukakis,HWbush)
# Election(1984,mondle,reagen)