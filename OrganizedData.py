import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import regex as re
from transformers import pipeline
# nltk.download('vader_lexicon')
electorateOpinion_abortion = pd.read_csv("/Users/jaxsonpaige/Inspirit/data/imagration.csv")
electorateOpinion_crime = pd.read_csv("/Users/jaxsonpaige/Inspirit/data/crimePolicies.csv")
electorateOpinion_defenseSpending = pd.read_csv("/Users/jaxsonpaige/Inspirit/data/defenseSpending.csv")
electorateOpinion_econemy = pd.read_csv("/Users/jaxsonpaige/Inspirit/data/ecenomicConfidance.csv")
electorateOpinion_education = pd.read_csv("/Users/jaxsonpaige/Inspirit/data/education.csv")
electorateOpinion_guns = pd.read_csv("/Users/jaxsonpaige/Inspirit/data/guns.csv")
electorateOpinion_healthcare = pd.read_csv("/Users/jaxsonpaige/Inspirit/data/healthcare.csv")
electorateOpinion_imagration = pd.read_csv("/Users/jaxsonpaige/Inspirit/data/imagration.csv")
electorateOpinion_taxes = pd.read_csv("/Users/jaxsonpaige/Inspirit/data/taxes.csv")
electorateData_party = pd.read_csv("/Users/jaxsonpaige/Inspirit/data/PartyAfiliation.csv")
electorateData_vote = pd.read_csv("/Users/jaxsonpaige/Inspirit/data/electionResults.csv")

bidenRawList=[]
trumpRawList=[]
obamaRawList=[]
andersonRawList=[]
reaganRawList=[]
bushRawList=[]
dukakisRawList=[]
kerryRawList=[]
clintonRawList=[]
HclintonRawList=[]
perotRawList=[]
carterRawList=[]
fordRawList=[]
doleRawList=[]
goreRawList=[]
kenedyRawList=[]
nixonRawList=[]
mcainRawList=[]
romneyRawList=[]
mondleRawList=[]

speeches = [
    "/Users/jaxsonpaige/Inspirit/data/speeches/anderson-reagon.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/biden-trump1.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/biden-trump2.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/biden-trump3.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/bush-clinton-parot1.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/bush-dukakis1.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/bush-dukakis2.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/bush-kerry1.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/bush-kerry2.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/bush-kerry3.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/carter-ford1.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/carter-ford2.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/carter-ford3.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/carter-reagon.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/clinton-bush-parot1.5.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/clinton-bush-parot2.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/clinton-bush-parot0.5.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/clinton-dole1.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/clinton-dole2.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/clinton-trump1.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/clinton-trump2.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/clinton-trump3.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/gore-bush1.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/gore-bush2.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/gore-bush3.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/kenedy-nixon1.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/kenedy-nixon2.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/kenedy-nixon3.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/mcain-obama1.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/mcain-obama2.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/mcain-obama3.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/nixon-kenedy.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/obama-romney1.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/obama-romney2.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/obama-romney3.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/reagan-mondle2.txt",
    "/Users/jaxsonpaige/Inspirit/data/speeches/reagon-mondle1.txt",
]

for i in speeches:
    with open(i,'r') as toRead:
        speech = toRead.read()
        parts = re.split(r'(\w+\s*:.*)', speech)
        for section in parts:
            if "BIDEN:" in section:
                bidenRawList.append(section)
            if "TRUMP:" in section:
                trumpRawList.append(section)
            if "OBAMA:" in section:
                obamaRawList.append(section)
            if "ANDERSON:" in section:
                andersonRawList.append(section)
            if "REAGAN:" in section:
                reaganRawList.append(section)
            if "BUSH:" in section:
                bushRawList.append(section)
            if "DUKAKIS:" in section:
                dukakisRawList.append(section)
            if "KERRY:" in section:
                kerryRawList.append(section)
            if "CLINTON:" in section:
                clintonRawList.append(section)
            if "HCLINTON:" in section:
                HclintonRawList.append(section)
            if "PEROT:" in section:
                perotRawList.append(section)
            if "CARTER:" in section:
                carterRawList.append(section)
            if "FORD:" in section:
                fordRawList.append(section)
            if "DOLE:" in section:
                doleRawList.append(section)
            if "GORE:" in section:
                goreRawList.append(section)
            if "KENEDY:" in section:
                kenedyRawList.append(section)
            if "NIXON:" in section:
                nixonRawList.append(section)
            if "MCCAIN:" in section:
                mcainRawList.append(section)
            if "ROMNEY:" in section:
                romneyRawList.append(section)
            if "MONDLE:" in section:
                mondleRawList.append(section)
# print(f"bidenrawlist: {bidenRawList}")

bidenRaw=' '.join(bidenRawList)
trumpRaw=' '.join(trumpRawList)
obamaRaw=' '.join(obamaRawList)
andersonRaw=' '.join(andersonRawList)
reaganRaw=' '.join(reaganRawList)
bushRaw=' '.join(bushRawList)
dukakisRaw=' '.join(dukakisRawList)
kerryRaw=' '.join(kenedyRawList)
clintonRaw=' '.join(clintonRawList)
HclintonRaw=' '.join(HclintonRawList)
perotRaw=' '.join(perotRawList)
carterRaw=' '.join(carterRawList)
fordRaw=' '.join(fordRawList)
doleRaw=' '.join(doleRawList)
goreRaw=' '.join(goreRawList)
kenedyRaw=' '.join(kenedyRawList)
nixonRaw=' '.join(nixonRawList)
mcainRaw=' '.join(mcainRawList)
romneyRaw=' '.join(romneyRawList)
mondleRaw=' '.join(mondleRawList)

# print(bidenRaw)

# bidenSentances = re.split(r'[.!?]\s*', bidenRaw)
# trumpSentances = re.split(r'[.!?]\s*', trumpRaw)
# obamaSentances = re.split(r'[.!?]\s*', obamaRaw)
# andersonSentances = re.split(r'[.!?]\s*', andersonRaw)
# reaganSentances = re.split(r'[.!?]\s*', reaganRaw)
# bushSentances = re.split(r'[.!?]\s*', bushRaw)
# dukakisSentances = re.split(r'[.!?]\s*', dukakisRaw)
# kerrySentances = re.split(r'[.!?]\s*', kerryRaw)
# clintonSentances = re.split(r'[.!?]\s*', clintonRaw)
# HclintonSentances = re.split(r'[.!?]\s*', HclintonRaw)
# perotSentances = re.split(r'[.!?]\s*', perotRaw)
# carterSentances = re.split(r'[.!?]\s*', carterRaw)
# fordSentances = re.split(r'[.!?]\s*', fordRaw)
# doleSentances = re.split(r'[.!?]\s*', doleRaw)
# goreSentances = re.split(r'[.!?]\s*', goreRaw)
# kenedySentances = re.split(r'[.!?]\s*', kenedyRaw)
# nixonSentances = re.split(r'[.!?]\s*', nixonRaw)
# mcainSentances = re.split(r'[.!?]\s*', mcainRaw)
# romneySentances = re.split(r'[.!?]\s*', romneyRaw)
# mondleSentances = re.split(r'[.!?]\s*', mondleRaw)

# classifier = pipeline("zero-shot-classification")
# labels = ["Self/myself/me/I", "Opponnent/he/she"]

# for sentance in bidenSentances:
#     classified = classifier(sentance, labels)