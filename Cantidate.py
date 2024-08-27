import pandas
import OrganizedData
from transformers import pipeline

class cantidate:
    def __init__(self, DATAraw, DATArawList, cantidate_name):
        #POSabortion, POScrime, POSdefenseSpending, POSeconemy, POSeducation, POSguns, POShealthcare, POSimagration, POSnationalSecurity, POStaxes,
        # self.abortion=POSabortion
        # self.defenseSpending=POSdefenseSpending
        # self.education=POSeducation
        # self.guns=POSguns
        # self.healthcare=POShealthcare 
        # self.imagration=POSimagration 
        # self.taxes=POStaxes 

        #not used
        self.raw=DATAraw

        #the data
        self.rawList=DATArawList
        # print(f"raw list in cantidate.py: {self.rawList}")
        # print("\n")

        self.name = cantidate_name

        classifier = pipeline("zero-shot-classification")
        labels = ["abortion","crime","millitary spending", "econemy", "education", "guns", "healthcare", "imagration", "defense", "other"]

        self.abortion_sentances = ["other"]
        self.crime_sentances = ["other"]
        self.millitarySpending_sentances = ["other"]
        self.education_sentances = ["other"]
        self.guns_sentances = ["other"]
        self.healthcare_sentances = ["other"]
        self.imagration_sentances = ["other"]
        self.defense_sentances = ["other"]

        # self.abortion_list = ["other"]
        # self.crime_list = ["other"]
        # self.millitarySpending_list = ["other"]
        # self.education_list = ["other"]
        # self.guns_list = ["other"]
        # self.healthcare_list = ["other"]
        # self.imagration_list = ["other"]
        # self.defense_list = ["other"]

        self.abortion_catagories = ["Abortion Legal under any", "Abortion Legal only under certain circumstances", "Abortion Illedgal in all circumstances", "Abortion no opinion","other"]
        self.crime_catagories = ["Crime rates Very satisfied","Crime rates Somewhat satisfied","Crime rates Somewhat dissatisfied","Crime rates Very dissatisfied","Crime rates No opinion","other"]
        self.millitarySpending_catagories = ["Millitary spending Too little", "Millitary spending Too much","other"]
        self.education_catagories = ["Education Completely satisfied","Education Somewhat satisfied","Education Somewhat dissatisfied","Education Completely dissatisfied","Education No opinion","other"]
        self.guns_catagories = ["More strict","Less strict","Kept as now","No opinion","other"]
        self.healthcare_catagories = ["healthcare governments responsibility","healthcare not governments responsibility","other"]
        self.imagration_catagories = ["Present level","Increased,Decreased","No opinion","other"]
        self.defense_catagories = ["defense Stronger than needs to be","defense Not strong enough","defense About right","other"]

        # self.abortion_scores = []
        # self.crime_scores = []
        # self.millitarySpending_scores = []
        # self.education_scores = []
        # self.guns_sentances = []
        # self.healthcare_scores = []
        # self.imagration_scores = []
        # self.defense_scores = []

        # print(f"\ncantidate: {self.name}\n")

        for i in self.rawList:
            result = classifier(i,labels)

            if result["labels"][0] == "abortion" and result["scores"][0] > 0.25:
                self.abortion_sentances.append(i)

            if result["labels"][0] == "crime" and result["scores"][0] > 0.25:
                self.crime_sentances.append(i)

            if result["labels"][0] == "millitary spending" and result["scores"][0] > 0.25:
                self.millitarySpending_sentances.append(i)

            if result["labels"][0] == "education" and result["scores"][0] > 0.25:
                self.education_sentances.append(i)

            if result["labels"][0] == "guns" and result["scores"][0] > 0.25:
                self.guns_sentances.append(i)

            if result["labels"][0] == "healthcare" and result["scores"][0] > 0.25:
                self.healthcare_sentances.append(i)

            if result["labels"][0] == "imagration" and result["scores"][0] > 0.25:   
                self.imagration_sentances.append(i)

            if result["labels"][0] == "defense" and result["scores"][0] > 0.25:
                self.defense_sentances.append(i)


        # for i in self.abortion_sentances:
        #     self.abortion_list.append(i)
        raw =' '.join(self.abortion_sentances)
        scores = classifier(raw, self.abortion_catagories)
        self.abortion_scores = scores

        # for i in self.crime_sentances:
        #     self.crime_list.append(i)
        raw =' '.join(self.crime_sentances)
        scores = classifier(raw, self.crime_catagories)
        self.crime_scores = scores

        # for i in self.millitarySpending_sentances:
        #     self.millitarySpending_list.append(i)
        raw =' '.join(self.millitarySpending_sentances)
        scores = classifier(raw, self.millitarySpending_catagories)
        self.millitarySpending_scores = scores

        # for i in self.education_sentances:
        #     self.education_list.append(i)
        raw =' '.join(self.education_sentances)
        scores = classifier(raw, self.education_catagories)
        self.education_scores = scores

        # for i in self.guns_sentances:
        #     self.guns_list.append(i)
        raw =' '.join(self.guns_sentances)
        scores = classifier(raw, self.guns_catagories)
        self.guns_scores = scores

        # for i in self.healthcare_sentances:
        #     self.healthcare_list.append(i)
        raw =' '.join(self.healthcare_sentances)
        scores = classifier(raw, self.healthcare_catagories)
        self.healthcare_scores = scores

        # for i in self.imagration_sentances:
        #     self.imagration_list.append(i)
        raw =' '.join(self.imagration_sentances)
        scores = classifier(raw, self.imagration_catagories)
        self.imagration_scores = scores

        # for i in self.defense_sentances:
        #     self.defense_list.append(i)
        raw =' '.join(self.defense_sentances)
        scores = classifier(raw, self.defense_catagories)
        self.defense_scores = scores

        # print(f"name: {self.name}")
        # print(f"abortion: {self.abortion_scores["labels"]} {self.abortion_scores["scores"]}")
        # print(f"crime: {self.crime_scores["labels"]} {self.crime_scores["scores"]}")
        # print(f"MillitarySpending: {self.millitarySpending_scores["labels"]} {self.millitarySpending_scores["scores"]}")
        # print(f"education: {self.education_scores["labels"]} {self.education_scores["scores"]}")
        # print(f"guns: {self.guns_scores["labels"]} {self.guns_scores["scores"]}")
        # print(f"healthcare: {self.healthcare_scores["labels"]} {self.healthcare_scores["scores"]}")
        # print(f"imagration: {self.imagration_scores["labels"]} {self.imagration_scores["scores"]}")
        # print(f"defense: {self.defense_scores["labels"]} {self.defense_scores["scores"]}")                                                                                         