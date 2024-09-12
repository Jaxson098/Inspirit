import pandas
import OrganizedData
from transformers import pipeline

class cantidate:
    def __init__(self, DATAraw, DATArawList, cantidate_name):

        classifier = pipeline("zero-shot-classification")
        # labels = ["abortion","crime","millitary spending", "econemy", "education", "guns", "healthcare", "imagration", "defense", "other"]

        abortion_catagories = ["Abortion should always Legal", "Abortion should be sometimes legal", "Abortion should be illegal", "no opinion about abortion"]
        crime_catagories = ["Very satisfied with Crime","Somewhat satisfied with crime","Somewhat dissatisfied with crime","Very dissatisfied with crime","No opinion about crime"]
        defense_spending_catagories = ["Too little Millitary spending", "Too much Millitary spending", "no opinion about Millitary spending"]
        education_catagories = ["very satisfied with education","Somewhat satisfied with Education","Somewhat dissatisfied with Education","Completely dissatisfied with Education","No opinion about Education"]
        gun_violence_catagories = ["More strict gun restrictions","Less strict gun restrictions","gun restrictions Kept as now","No opinion about gun restrictions"]
        healthcare_catagories = ["healthcare is governments responsibility","healthcare is not governments responsibility", "no opinion about healthcare"]
        immigration_catagories = ["imagration should be kept at Present level","imagration should be Increased","imagration should be Decreased","No opinion about imagration"]
        national_security_catagories = ["national security Stronger than needs to be","national security Not strong enough","national security About right","no opinion about national security"]

        abortion_txt = f'/home/jaxson/Inspirit/rawText/{cantidate_name}/abortion.txt'
        crime_txt = f'/home/jaxson/Inspirit/rawText/{cantidate_name}/crime.txt'
        defense_spending_txt = f'/home/jaxson/Inspirit/rawText/{cantidate_name}/defense spending.txt'
        education_txt = f'/home/jaxson/Inspirit/rawText/{cantidate_name}/education.txt'
        gun_violence_txt = f'/home/jaxson/Inspirit/rawText/{cantidate_name}/gun violence.txt'
        healthcare_txt = f'/home/jaxson/Inspirit/rawText/{cantidate_name}/healthcare.txt'
        immigration_txt = f'/home/jaxson/Inspirit/rawText/{cantidate_name}/immigration.txt'
        national_security_txt = f'/home/jaxson/Inspirit/rawText/{cantidate_name}/national security.txt'

        labels=[]

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
                    score = classifier(line, catagories)
                    label_list.append(score["labels"][0])

        scoring(abortion_txt,abortion_catagories,abortion_labels)
        scoring(crime_txt,crime_catagories,crime_labels)
        scoring(defense_spending_txt,defense_spending_catagories,defense_spending_labels)
        scoring(education_txt,education_catagories,education_labels)
        scoring(gun_violence_txt,gun_violence_catagories,gun_violence_labels)
        scoring(healthcare_txt,healthcare_catagories,healthcare_labels)
        scoring(immigration_txt,immigration_catagories,immigration_labels)
        scoring(national_security_txt,national_security_catagories,national_security_labels)

        raw =' '.join(self.abortion_sentances)
        scores = classifier(raw, self.abortion_catagories)
        self.abortion_scores = scores

        raw =' '.join(self.crime_sentances)
        scores = classifier(raw, self.crime_catagories)
        self.crime_scores = scores

        raw =' '.join(self.millitarySpending_sentances)
        scores = classifier(raw, self.millitarySpending_catagories)
        self.millitarySpending_scores = scores

        raw =' '.join(self.education_sentances)
        scores = classifier(raw, self.education_catagories)
        self.education_scores = scores

        raw =' '.join(self.guns_sentances)
        scores = classifier(raw, self.guns_catagories)
        self.guns_scores = scores

        raw =' '.join(self.healthcare_sentances)
        scores = classifier(raw, self.healthcare_catagories)
        self.healthcare_scores = scores

        raw =' '.join(self.imagration_sentances)
        scores = classifier(raw, self.imagration_catagories)
        self.imagration_scores = scores

        raw =' '.join(self.defense_sentances)
        scores = classifier(raw, self.defense_catagories)
        self.defense_scores = scores