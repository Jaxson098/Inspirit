from bs4 import BeautifulSoup
import requests
import regex as re

keyWords = ["abortion", '"crime"+"crime rates"', '"millitary spending"+"defense spending"+"defense"', "education", '"gun violence"+"gun control"', "healthcare+medicare", "immigration", '"national security"']
flagWords = ["abortion", "crime","crime rates", "millitary spending","defense spending", "education", "gun violence","gun control", "healthcare","medicare", "immigration", "national security"]

pattern = r'^\b[A-Z]+\b'

class scrape:
    def __init__(self, canName, canNum):

        links = []
        sentances = {word: [] for word in flagWords}    
        
        def scrapeLinks():
            for i in keyWords:
                url = f"https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2={i}&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2={canNum}&category2%5B%5D=74&category2%5B%5D=73&category2%5B%5D=8&category2%5B%5D=52&category2%5B%5D=46&category2%5B%5D=48&category2%5B%5D=45&category2%5B%5D=65&category2%5B%5D=49&items_per_page=100"
                print(url)
                response = requests.get(url)  
                soup = BeautifulSoup(response.content, 'html.parser')
                tr_tags = soup.find_all('tr', {'class': ['even', 'odd']})
                for tr in tr_tags:
                    td_title = tr.find('td', class_='views-field views-field-title')
                    if td_title:
                        link = td_title.a.get('href')
                        if link:
                            links.append(link)
            return links

        def getP():
            for link in links:
                url = f"https://www.presidency.ucsb.edu{link}"
                print(url)
                response = requests.get(url) 
                soup = BeautifulSoup(response.content, 'html.parser') 
                p_tags = soup.find_all('p')
                for p in p_tags:
                    cleanText = re.sub('<.*?>', '', str(p))
                    for word in flagWords:
                        if word in cleanText and 'Q.' not in cleanText and bool(re.search(pattern, cleanText)) == False:
                            print(f"word: {word} sentances apended: {cleanText} \n")
                            sentances[word].append(cleanText)

        scrapeLinks()
        getP()

        for key, value in sentances.items():
            with open(f"/home/jaxson/Inspirit/rawText/{canName}/{key}.txt", 'w') as file:
                for item in value:
                    file.write(f"{item}\n")

class nonPrezScrape:
    def __init__(self, canName, canNum):

        links = []
        sentances = {word: [] for word in flagWords}    
        
        def scrapeLinks():
            for i in keyWords:
                url = f"https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2={i}&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=&items_per_page=100&f%5B0%5D=field_docs_person%{canNum}"
                print(url)
                response = requests.get(url)  
                soup = BeautifulSoup(response.content, 'html.parser')
                tr_tags = soup.find_all('tr', {'class': ['even', 'odd']})
                for tr in tr_tags:
                    td_title = tr.find('td', class_='views-field views-field-title')
                    if td_title:
                        link = td_title.a.get('href')
                        if link:
                            links.append(link)
            return links

        def getP():
            for link in links:
                url = f"https://www.presidency.ucsb.edu{link}"
                print(url)
                response = requests.get(url) 
                soup = BeautifulSoup(response.content, 'html.parser') 
                p_tags = soup.find_all('p')
                for p in p_tags:
                    cleanText = re.sub('<.*?>', '', str(p))
                    for word in flagWords:
                        if word in cleanText and 'Q.' not in cleanText and bool(re.search(pattern, cleanText)) == False:
                            print(f"word: {word} sentances apended: {cleanText} \n")
                            sentances[word].append(cleanText)

        scrapeLinks()
        getP()

        for key, value in sentances.items():
            with open(f"/home/jaxson/Inspirit/rawText/{canName}/{key}.txt", 'w') as file:
                for item in value:
                    file.write(f"{item}\n")


# scrape("biden","200320")
# scrape("trump","200301")
# scrape("obama","200300")
# scrape("reagen","200296")
# scrape("Wbush","200299")
# scrape("HWbush","200297")


#cant find anything:

# nonPrezScrape("mondle",)
# nonPrezScrape("dukakis",)
# nonPrezScrape("kerry",)
# nonPrezScrape("gore",)



# scrape("clinton","200298")
nonPrezScrape("Hclinton","3A200317")
# scrape("carter","200295")
nonPrezScrape("dole","3A200312")
nonPrezScrape("mccain","3A200315")
nonPrezScrape("romney","3A200326")