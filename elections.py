import pandas as pd
import csv
import cantidatesData

abortion_catagories = ["Abortion Legal under any", "Abortion Legal only under certain circumstances", "Abortion Illedgal in all circumstances", "Abortion no opinion"]
crime_catagories = ["Crime rates Very satisfied","Crime rates Somewhat satisfied","Crime rates Somewhat dissatisfied","Crime rates Very dissatisfied","Crime rates No opinion"]
millitarySpending_catagories = ["Millitary spending Too little", "Millitary spending Too much"]
education_catagories = ["Education Completely satisfied","Education Somewhat satisfied","Education Somewhat dissatisfied","Education Completely dissatisfied","Education No opinion"]
guns_catagories = ["More strict","Less strict","Kept as now","No opinion"]
healthcare_catagories = ["healthcare governments responsibility","healthcare not governments responsibility"]
imagration_catagories = ["Present level","Increased,Decreased","No opinion"]
defense_catagories = ["defense Stronger than needs to be","defense Not strong enough","defense About right"]

abortion_dict_1 = {label: [] for label in abortion_catagories}
crime_dict_1 = {label: [] for label in crime_catagories}
millitarySpending_dict_1 = {label: [] for label in millitarySpending_catagories}
education_dict_1 = {label: [] for label in education_catagories}
guns_dict_1 = {label: [] for label in guns_catagories}
healthcare_dict_1 = {label: [] for label in healthcare_catagories}
imagration_dict_1 = {label: [] for label in imagration_catagories}
defense_dict_1 = {label: [] for label in defense_catagories}

abortion_dict_2 = {label: [] for label in abortion_catagories}
crime_dict_2 = {label: [] for label in crime_catagories}
millitarySpending_dict_2 = {label: [] for label in millitarySpending_catagories}
education_dict_2 = {label: [] for label in education_catagories}
guns_dict_2 = {label: [] for label in guns_catagories}
healthcare_dict_2 = {label: [] for label in healthcare_catagories}
imagration_dict_2 = {label: [] for label in imagration_catagories}
defense_dict_2 = {label: [] for label in defense_catagories}

abortionPoll_dict = {label: [] for label in abortion_catagories}
crimePoll_dict = {label: [] for label in crime_catagories}
millitarySpendingPoll_dict = {label: [] for label in millitarySpending_catagories}
educationPoll_dict = {label: [] for label in education_catagories}
gunsPoll_dict = {label: [] for label in guns_catagories}
healthcarePoll_dict = {label: [] for label in healthcare_catagories}
imagrationPoll_dict = {label: [] for label in imagration_catagories}
defensePoll_dict = {label: [] for label in defense_catagories}

def getPollData(path, year):
    with open(path, mode='r') as file:
        reader = csv.reader(file)
        rows = []
            
        for row in reader:
            if str(year) in row[0]: 
                rows.append(row)
    return rows[-1]


# abortionPoll = getPollData('/home/jaxson/Inspirit/data/abortion.csv', year='2016')
# print(abortionPoll)

def format(dict, labels, scores):
  for i in range(len(labels)):
    dict[labels[i]].append(scores[i])

class Election:
    def __init__(self, election_year, cantidate_1, cantidate_2, csvName):
        
        self.year = election_year

        abortionPoll = getPollData('/home/jaxson/Inspirit/data/abortion.csv', year=self.year)
        crimePoll = getPollData('/home/jaxson/Inspirit/data/crimePolicies.csv', year=self.year)
        millitarySpendingPoll = getPollData('/home/jaxson/Inspirit/data/defenseSpending.csv', year=self.year)
        educationPoll = getPollData('/home/jaxson/Inspirit/data/education.csv', year=self.year)
        gunsPoll = getPollData('/home/jaxson/Inspirit/data/guns.csv', year=self.year)
        healthcarePoll = getPollData('/home/jaxson/Inspirit/data/healthcare.csv', year=self.year)
        imagrationPoll = getPollData('/home/jaxson/Inspirit/data/imagration.csv', year=self.year)
        defensePoll = getPollData('/home/jaxson/Inspirit/data/nationalSecurity.csv', year=self.year)

        format(abortion_dict_1, abortion_catagories, cantidate_1.abortion_scores["scores"])
        format(crime_dict_1, crime_catagories, cantidate_1.crime_scores["scores"])
        format(millitarySpending_dict_1, millitarySpending_catagories, cantidate_1.millitarySpending_scores["scores"])
        format(education_dict_1, education_catagories, cantidate_1.education_scores["scores"])
        format(guns_dict_1, guns_catagories, cantidate_1.guns_scores["scores"])
        format(healthcare_dict_1, healthcare_catagories, cantidate_1.healthcare_scores["scores"])
        format(imagration_dict_1, imagration_catagories, cantidate_1.imagration_scores["scores"])
        format(defense_dict_1, defense_catagories, cantidate_1.defense_scores["scores"])

        format(abortion_dict_2, abortion_catagories, cantidate_2.abortion_scores["scores"])
        format(crime_dict_2, crime_catagories, cantidate_2.crime_scores["scores"])
        format(millitarySpending_dict_2, millitarySpending_catagories, cantidate_2.millitarySpending_scores["scores"])
        format(education_dict_2, education_catagories, cantidate_2.education_scores["scores"])
        format(guns_dict_2, guns_catagories, cantidate_2.guns_scores["scores"])
        format(healthcare_dict_2, healthcare_catagories, cantidate_2.healthcare_scores["scores"])
        format(imagration_dict_2, imagration_catagories, cantidate_2.imagration_scores["scores"])
        format(defense_dict_2, defense_catagories, cantidate_2.defense_scores["scores"])

        format(abortionPoll_dict, abortion_catagories, abortionPoll)
        format(crimePoll_dict, crime_catagories, crimePoll)
        format(millitarySpendingPoll_dict, millitarySpending_catagories, millitarySpendingPoll)
        format(educationPoll_dict, education_catagories, educationPoll)
        format(gunsPoll_dict, guns_catagories, gunsPoll)
        format(healthcarePoll_dict, healthcare_catagories, healthcarePoll)
        format(imagrationPoll_dict, imagration_catagories, imagrationPoll)
        format(defensePoll_dict, defense_catagories, defensePoll)

        str(abortion_dict_1)
        str(crime_dict_1)
        str(millitarySpending_dict_1)
        str(education_dict_1)
        str(guns_dict_1)
        str(healthcare_dict_1)
        str(imagration_dict_1)
        str(defense_dict_1)

        str(abortion_dict_2)
        str(crime_dict_2)
        str(millitarySpending_dict_2)
        str(education_dict_2)
        str(guns_dict_2)
        str(healthcare_dict_2)
        str(imagration_dict_2)
        str(defense_dict_2)

        str(abortionPoll_dict)
        str(crimePoll_dict)
        str(millitarySpendingPoll_dict)
        str(educationPoll_dict)
        str(gunsPoll_dict)
        str(healthcarePoll_dict)
        str(imagrationPoll_dict)
        str(defensePoll_dict)

        finalData = {'year': self.year, 'can1': cantidate_1.name, 'can2': cantidate_2.name, 
                     'can1 abortion': abortion_dict_1, 'can2 abortion:': abortion_dict_2, 'poll abortion': abortionPoll_dict,
                     'can1 crime': crime_dict_1, 'can2 crime:': crime_dict_2, 'poll crime': crimePoll_dict,
                     'can1 millitary spending': millitarySpending_dict_1, 'can2 millitary spending:': millitarySpending_dict_2, 'poll millitary spending': millitarySpendingPoll_dict,
                     'can1 education': education_dict_1, 'can2 education:': education_dict_2, 'poll education': educationPoll_dict,
                     'can1 guns': guns_dict_1, 'can2 guns:': guns_dict_2, 'poll guns': gunsPoll_dict,
                     'can1 healthcare': healthcare_dict_1, 'can2 healthcare:': healthcare_dict_2, 'poll healthcare': healthcarePoll_dict,
                     'can1 imagration': imagration_dict_1, 'can2 imagration:': imagration_dict_1, 'poll imagration': imagrationPoll_dict,
                     'can1 defense': defense_dict_1, 'can2 defense:': defense_dict_2, 'poll defense': defensePoll_dict
                     }
        
        df = pd.DataFrame([finalData])
        df.to_csv(csvName, index=False, header=False)  



# Election('2016', cantidatesData.Hclinton, cantidatesData.trump)
# Election('2020', cantidatesData.biden, cantidatesData.trump, '2020Elec.csv')
Election('2012', cantidatesData.obama, cantidatesData.romney, '2012Elec.csv')
# Election('2004', cantidatesData.obama, cantidatesData.mccain, '2004Elec.csv')   