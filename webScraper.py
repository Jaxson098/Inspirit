from bs4 import BeautifulSoup
import requests
import regex as re

keyWords = ["abortion", '"crime"+"crime rates"', '"millitary spending"+"defense spending"+"defense"', "education", '"gun violence"+"gun control"', "healthcare+medicare", "immigration", '"national security"']
flagWords = ["abortion", "crime","crime rates", "millitary spending","defense spending", "education", "gun violence","gun control", "healthcare","medicare", "immigration", "national security"]
links = []
sentances = {word: [] for word in flagWords}

def scrapeLinks():
    for i in keyWords:
        url = f"https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2={i}&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200294&category2%5B%5D=74&category2%5B%5D=73&category2%5B%5D=8&category2%5B%5D=52&category2%5B%5D=46&category2%5B%5D=48&category2%5B%5D=45&category2%5B%5D=65&category2%5B%5D=64&category2%5B%5D=49&items_per_page=100"
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
                if word in cleanText and "Q." not in cleanText:
                    print(f"word: {word} sentances apended: {cleanText} \n")
                    sentances[word].append(cleanText)

scrapeLinks()
getP()

for key, value in sentances.items():

    with open(f"/home/jaxson/Inspirit/rawText/ford/{key}.txt", 'w') as file:
        for item in value:
            file.write(f"{item}\n")

#obamam: 200300
#bush: 200299
#clinton: 200298
#reagen 200296
#carter: 200295
#ford: 200294
#nixion: 200293
