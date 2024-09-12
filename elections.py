import pandas as pd
import csv
import cantidatesData

abortion_catagories = ["Abortion should always Legal", "Abortion should be sometimes legal", "Abortion should be illegal", "no opinion about abortion"]
crime_catagories = ["Very satisfied with Crime","Somewhat satisfied with crime","Somewhat dissatisfied with crime","Very dissatisfied with crime","No opinion about crime"]
millitarySpending_catagories = ["Too little Millitary spending", "Too much Millitary spending", "no opinion about Millitary spending"]
education_catagories = ["very satisfied with education","Somewhat satisfied with Education","Somewhat dissatisfied with Education","Completely dissatisfied with Education","No opinion about Education"]
guns_catagories = ["More strict gun restrictions","Less strict gun restrictions","gun restrictions Kept as now","No opinion about gun restrictions"]
healthcare_catagories = ["healthcare is governments responsibility","healthcare is not governments responsibility", "no opinion about healthcare"]
imagration_catagories = ["imagration should be kept at Present level","imagration should be Increased","imagration should be Decreased","No opinion about imagration"]
defense_catagories = ["national security Stronger than needs to be","national security Not strong enough","national security About right","no opinion about national security"]

def getPollData(path, year):
    with open(path, mode='r') as file:
        reader = csv.reader(file)
        rows = []
            
        for row in reader:
            if str(year) in row[0]: 
                rows.append(row)
                
    yearData = rows[-1]
    maxValue = max(yearData)
    labelIndex = yearData.index(maxValue) -1
    return f"{maxValue} {labelIndex}"

class Election:
    def __init__(self, election_year, cantidate_1, cantidate_2):

        abortion_poll_percentage = getPollData('/home/jaxson/Inspirit/data/abortion.csv', year=self.year)
        crime_poll_percentage = getPollData('/home/jaxson/Inspirit/data/crimePolicies.csv', year=self.year)
        millitarySpending_poll_percentage = getPollData('/home/jaxson/Inspirit/data/defenseSpending.csv', year=self.year)
        education_poll_percentage = getPollData('/home/jaxson/Inspirit/data/education.csv', year=self.year)
        guns_poll_percentage = getPollData('/home/jaxson/Inspirit/data/guns.csv', year=self.year)
        healthcare_poll_percentage = getPollData('/home/jaxson/Inspirit/data/healthcare.csv', year=self.year)
        imagration_poll_percentage = getPollData('/home/jaxson/Inspirit/data/imagration.csv', year=self.year)
        defense_poll_percentage = getPollData('/home/jaxson/Inspirit/data/nationalSecurity.csv', year=self.year)

        can1Abortion = abortion_catagories.index(cantidate_1.abortion_scores["labels"][0])
        can1Crime = crime_catagories.index(cantidate_1.crime_scores["labels"][0])
        can1MillitarySpending = millitarySpending_catagories.index(cantidate_1.millitarySpending_scores["labels"][0])
        can1Education = education_catagories.index(cantidate_1.education_scores["labels"][0])
        can1Guns = guns_catagories.index(cantidate_1.guns_scores["labels"][0])
        can1Healthcare = healthcare_catagories.index(cantidate_1.healthcare_scores["labels"][0])
        can1Imagration = imagration_catagories.index(cantidate_1.imagration_scores["labels"][0])
        can1Defense = defense_catagories.index(cantidate_1.defense_scores["labels"][0])

        can2Abortion = abortion_catagories.index(cantidate_2.abortion_scores["labels"][0])
        can2Crime = crime_catagories.index(cantidate_2.crime_scores["labels"][0])
        can2MillitarySpending = millitarySpending_catagories.index(cantidate_2.millitarySpending_scores["labels"][0])
        can2Education = education_catagories.index(cantidate_2.education_scores["labels"][0])
        can2Guns = guns_catagories.index(cantidate_1.guns_scores["labels"][0])
        can2Healthcare = healthcare_catagories.index(cantidate_2.healthcare_scores["labels"][0])
        can2Imagration = imagration_catagories.index(cantidate_2.imagration_scores["labels"][0])
        can2Defense = defense_catagories.index(cantidate_2.defense_scores["labels"][0])

        data = [can1Abortion,can2Abortion,abortionPoll,
                can1Crime,can2Crime,crimePoll,
                can1MillitarySpending,can2MillitarySpending,millitarySpendingPoll,
                can1Education,can2Education,educationPoll,
                can1Guns,can2Guns,gunsPoll,
                can1Healthcare,can2Healthcare,healthcarePoll,
                can1Imagration,can2Imagration,imagrationPoll,
                can1Defense,can2Defense,defensePoll]
        
        with open('./election.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
            writer.writerow(data)

        # df = pd.DataFrame(data)
        # df.to_csv(csvName, index=False)

        # format(abortion_dict_1, abortion_catagories, cantidate_1.abortion_scores["scores"])
        # format(crime_dict_1, crime_catagories, cantidate_1.crime_scores["scores"])
        # format(millitarySpending_dict_1, millitarySpending_catagories, cantidate_1.millitarySpending_scores["scores"])
        # format(education_dict_1, education_catagories, cantidate_1.education_scores["scores"])
        # format(guns_dict_1, guns_catagories, cantidate_1.guns_scores["scores"])
        # format(healthcare_dict_1, healthcare_catagories, cantidate_1.healthcare_scores["scores"])
        # format(imagration_dict_1, imagration_catagories, cantidate_1.imagration_scores["scores"]) 
        # format(defense_dict_1, defense_catagories, cantidate_1.defense_scores["scores"])

        # format(abortion_dict_2, abortion_catagories, cantidate_2.abortion_scores["scores"])
        # format(crime_dict_2, crime_catagories, cantidate_2.crime_scores["scores"])
        # format(millitarySpending_dict_2, millitarySpending_catagories, cantidate_2.millitarySpending_scores["scores"])
        # format(education_dict_2, education_catagories, cantidate_2.education_scores["scores"])
        # format(guns_dict_2, guns_catagories, cantidate_2.guns_scores["scores"])
        # format(healthcare_dict_2, healthcare_catagories, cantidate_2.healthcare_scores["scores"])
        # format(imagration_dict_2, imagration_catagories, cantidate_2.imagration_scores["scores"])
        # format(defense_dict_2, defense_catagories, cantidate_2.defense_scores["scores"])

        # format(abortionPoll_dict, abortion_catagories, abortionPoll)
        # format(crimePoll_dict, crime_catagories, crimePoll)
        # format(millitarySpendingPoll_dict, millitarySpending_catagories, millitarySpendingPoll)
        # format(educationPoll_dict, education_catagories, educationPoll)
        # format(gunsPoll_dict, guns_catagories, gunsPoll)
        # format(healthcarePoll_dict, healthcare_catagories, healthcarePoll)
        # format(imagrationPoll_dict, imagration_catagories, imagrationPoll)
        # format(defensePoll_dict, defense_catagories, defensePoll)

        # str(abortion_dict_1)
        # str(crime_dict_1)
        # str(millitarySpending_dict_1)
        # str(education_dict_1)
        # str(guns_dict_1)
        # str(healthcare_dict_1)
        # str(imagration_dict_1)
        # str(defense_dict_1)

        # str(abortion_dict_2)
        # str(crime_dict_2)
        # str(millitarySpending_dict_2)
        # str(education_dict_2)
        # str(guns_dict_2)
        # str(healthcare_dict_2)
        # str(imagration_dict_2)
        # str(defense_dict_2)

        # str(abortionPoll_dict)
        # str(crimePoll_dict)
        # str(millitarySpendingPoll_dict)
        # str(educationPoll_dict)
        # str(gunsPoll_dict)
        # str(healthcarePoll_dict)
        # str(imagrationPoll_dict)
        # str(defensePoll_dict)

        # finalData = {'year': self.year, 'can1': cantidate_1.name, 'can2': cantidate_2.name, 
        #              'can1 abortion': abortion_dict_1, 'can2 abortion:': abortion_dict_2, 'poll abortion': abortionPoll_dict,
        #              'can1 crime': crime_dict_1, 'can2 crime:': crime_dict_2, 'poll crime': crimePoll_dict,
        #              'can1 millitary spending': millitarySpending_dict_1, 'can2 millitary spending:': millitarySpending_dict_2, 'poll millitary spending': millitarySpendingPoll_dict,
        #              'can1 education': education_dict_1, 'can2 education:': education_dict_2, 'poll education': educationPoll_dict,
        #              'can1 guns': guns_dict_1, 'can2 guns:': guns_dict_2, 'poll guns': gunsPoll_dict,
        #              'can1 healthcare': healthcare_dict_1, 'can2 healthcare:': healthcare_dict_2, 'poll healthcare': healthcarePoll_dict,
        #              'can1 imagration': imagration_dict_1, 'can2 imagration:': imagration_dict_1, 'poll imagration': imagrationPoll_dict,
        #              'can1 defense': defense_dict_1, 'can2 defense:': defense_dict_2, 'poll defense': defensePoll_dict
        #              }
        
        # df.to_csv(csvName, index=False, header=False)  


# Election('2020', cantidatesData.biden, cantidatesData.trump)
# Election('2016', cantidatesData.Hclinton, cantidatesData.trump)
# Election('2012', cantidatesData.obama, cantidatesData.romney)
# Election('2004', cantidatesData.obama, cantidatesData.mccain)   