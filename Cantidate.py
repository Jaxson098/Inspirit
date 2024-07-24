import pandas
import OrganizedData
from transformers import pipeline

class cantidate:
    def __init__(self, DATAraw, DATArawList):
        #POSabortion, POScrime, POSdefenseSpending, POSeconemy, POSeducation, POSguns, POShealthcare, POSimagration, POSnationalSecurity, POStaxes,
        # self.abortion=POSabortion
        # self.defenseSpending=POSdefenseSpending
        # self.education=POSeducation
        # self.guns=POSguns
        # self.healthcare=POShealthcare 
        # self.imagration=POSimagration 
        # self.taxes=POStaxes 
        self.raw=DATAraw
        self.rawList=DATArawList

        classifier = pipeline("zero-shot-classification")
        labels = ["abortion","crime","millitary spending", "econemy", "education", "guns", "healthcare", "imagration", "defense"]

        self.abortion_sentances = []
        self.crime_sentances = []
        self.millitarySpending_sentances = []
        # self.econemy_sentances = []
        self.education_sentances = []
        self.guns_sentances = []
        self.healthcare_sentances = []
        self.imagration_sentances = []
        self.defense_sentances = []

        self.abortion_list = []
        self.crime_list = []
        self.millitarySpending_list = []
        self.education_list = []
        self.guns_list = []
        self.healthcare_list = []
        self.imagration_list = []
        self.defense_list = []

        self.abortion_catagories = ["Abortion Legal under any", "Abortion Legal only under certain circumstances", "Abortion Illedgal in all circumstances", "Abortion no opinion"]
        self.crime_catagories = ["Crime rates Very satisfied","Crime rates Somewhat satisfied","Crime rates Somewhat dissatisfied","Crime rates Very dissatisfied","Crime rates No opinion"]
        self.millitarySpending_catagories = ["Millitary spending Too little", "Millitary spending Too much"]
        # self.econemy_catagories = []
        self.education_catagories = ["Education Completely satisfied","Education Somewhat satisfied","Education Somewhat dissatisfied","Education Completely dissatisfied","Education No opinion"]
        self.guns_catagories = ["More strict","Less strict","Kept as now","No opinion"]
        self.healthcare_catagories = ["healthcare governments responsibility","healthcare not governments responsibility"]
        self.imagration_catagories = ["Present level","Increased,Decreased","No opinion"]
        self.defense_catagories = ["defense Stronger than needs to be","defense Not strong enough","defense About right"]

        self.abortion_scores = []
        self.crime_scores = []
        self.millitarySpending_scores = []
        self.education_scores = []
        self.guns_sentances = []
        self.healthcare_scores = []
        self.imagration_scores = []
        self.defense_scores = []

        for i in self.rawList:
            result = classifier(i,labels)
            if result["labels"][0] == "abortion":
                self.abortion_sentances.append(i)

            if result["labels"][0] == "crime":
                self.crime_sentances.append(i)

            if result["labels"][0] == "millitary spending":
                self.millitarySpending_sentances.append(i)

            # if result["labels"][0] == "econemy":
            #     self.econemy_sentances.append(i)

            if result["labels"][0] == "education":
                self.education_sentances.append(i)

            if result["labels"][0] == "guns":
                self.guns_sentances.append(i)

            if result["labels"][0] == "healthcare":
                self.healthcare_sentances.append(i)

            if result["labels"][0] == "imagration":
                self.imagration_sentances.append(i)

            if result["labels"][0] == "defense":
                self.defense_sentances.append(i)

        for i in self.abortion_sentances:
            self.abortion_list.append(i)
        raw =' '.join(self.abortion_list)
        scores = classifier(raw, self.abortion_catagories)
        self.abortion_scores = scores

        for i in self.crime_sentances:
            self.crime_list.append(i)
        raw =' '.join(self.crime_list)
        scores = classifier(raw, self.abortion_catagories)
        self.crime_scores = scores

        for i in self.millitarySpending_sentances:
            self.millitarySpending_list.append(i)
        raw =' '.join(self.millitarySpending_list)
        scores = classifier(raw, self.millitarySpending_catagories)
        self.millitarySpending_scores = scores

        # for i in self.econemy_sentances:
        #     list = []
        #     list.append(i)
        #     raw =' '.join(list)
        # scores = classifier(raw, self.econemy_catagories)
        #self._scores = scores

        for i in self.education_sentances:
            self.education_list.append(i)
        raw =' '.join(self.education_list)
        scores = classifier(raw, self.education_catagories)
        self.education_scores = scores

        for i in self.guns_sentances:
            self.guns_list.append(i)
        raw =' '.join(self.guns_list)
        scores = classifier(raw, self.guns_catagories)
        self.guns_scores = scores

        for i in self.healthcare_sentances:
            self.healthcare_list.append(i)
        raw =' '.join(self.healthcare_list)
        scores = classifier(raw, self.healthcare_catagories)
        self.healthcare_scores = scores

        for i in self.imagration_sentances:
            self.imagration_list.append(i)
        raw =' '.join(self.imagration_list)
        scores = classifier(raw, self.imagration_catagories)
        self.imagration_scores = scores

        for i in self.defense_sentances:
            self.defense_list.append(i)
        raw =' '.join(self.defense_list)
        scores = classifier(raw, self.defense_catagories)
        self.defense_scores = scores

        print(f"abortion: {self.abortion_scores["labels"]} {self.abortion_scores["scores"]}")
        print(f"crime: {self.crime_scores["labels"]} {self.crime_scores["scores"]}")
        print(f"MillitarySpending: {self.millitarySpending_scores["labels"]} {self.millitarySpending_scores["scores"]}")
        print(f"education: {self.education_scores["labels"]} {self.education_scores["scores"]}")
        print(f"guns: {self.guns_sentances["labels"]} {self.guns_sentances["scores"]}")
        print(f"healthcare: {self.healthcare_scores["labels"]} {self.healthcare_scores["scores"]}")
        print(f"imagration: {self.imagration_scores["labels"]} {self.imagration_scores["scores"]}")
        print(f"defense: {self.defense_scores["labels"]} {self.defense_scores["scores"]}")                                                                                         