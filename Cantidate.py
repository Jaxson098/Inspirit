import pandas
import OrganizedData
from transformers import pipeline

class cantidate:
    def __init__(self, POSabortion, POScrime, POSdefenseSpending, POSeconemy, POSeducation, POSguns, POShealthcare, POSimagration, POSnationalSecurity, POStaxes, DATAraw, DATArawList):
        self.abortion=POSabortion
        self.defenseSpending=POSdefenseSpending
        self.education=POSeducation
        self.guns=POSguns
        self.healthcare=POShealthcare 
        self.imagration=POSimagration 
        self.taxes=POStaxes 
        self.raw=DATAraw
        self.rawList=DATArawList

        classifier = pipeline("zero-shot-classification")
        labels = ["crime","healthcare/medicine/prescription","defense/security/national security/war/nuke", "other"]

        self.cirmeFreq = 0
        self.healthcareFreq = 0
        self.nationalSecurityFreq = 0
        self.otherFreq = 0

        for i in self.rawList:
            result = classifier(i,labels)
            if result["labels"][0] == "crime":
                self.cirmeFreq += 1
            if result["labels"][0] == "healthcare/medicine/prescription":
                self.healthcareFreq += 1
            if result["labels"][0] == "defense/security/national security/war":
                self.nationalSecurityFreq += 1
            if result["labels"][0] == "other":
                self.otherFreq += 1
