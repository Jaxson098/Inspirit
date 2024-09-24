from hugchat import hugchat
from hugchat.login import Login


class cantidate:
    def __init__(cantidate_name):

        # classifier = pipeline("zero-shot-classification")
        # labels = ["abortion","crime","millitary spending", "econemy", "education", "guns", "healthcare", "imagration", "defense", "other"]

        abortion_catagories = ['"Abortion should always Legal", "Abortion should be sometimes legal", "Abortion should be illegal", "no opinion about abortion"']
        crime_catagories = ['"satisfied with crime","dissatisfied with crime","No opinion about crime"']
        millitarySpending_catagories = ['"Too little Millitary spending", "Too much Millitary spending", "no opinion about Millitary spending"']
        education_catagories = ['"very satisfied with education","Somewhat satisfied with Education","Somewhat dissatisfied with Education","Completely dissatisfied with Education","No opinion about Education"']
        guns_catagories = ['"More strict gun restrictions","Less strict gun restrictions","gun restrictions Kept as now","No opinion about gun restrictions"']
        healthcare_catagories = ['"healthcare is governments responsibility","healthcare is not governments responsibility", "no opinion about healthcare"']
        imagration_catagories = ['"imagration should be kept at Present level","imagration should be Increased","imagration should be Decreased","No opinion about imagration"']
        defense_catagories = ['"national security Stronger than needs to be","national security Not strong enough","national security About right","no opinion about national security"']

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

        sign = Login('jaxson.paige@lejardinacademy.org', 'KillerKiaSoul098')
        cookies = sign.login()
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict(), default_llm='meta-llama/Meta-Llama-3.1-70B-Instruct')

        def scoring(path,catagories,label_list):
            with open(path, "r") as file:
                for line in file:
                    score = chatbot.chat(f'''do not answer with anything but one of these categories: {catagories}. which of those categories do you thin fits this sentence best: {line}''')
                    label_list.append(str(score))

        scoring(abortion_txt,abortion_catagories,abortion_labels)
        scoring(crime_txt,crime_catagories,crime_labels)
        scoring(defense_spending_txt,millitarySpending_catagories,defense_spending_labels)
        scoring(education_txt,education_catagories,education_labels)
        scoring(gun_violence_txt,guns_catagories,gun_violence_labels)
        scoring(healthcare_txt,healthcare_catagories,healthcare_labels)
        scoring(immigration_txt,imagration_catagories,immigration_labels)
        scoring(national_security_txt,defense_catagories,national_security_labels)