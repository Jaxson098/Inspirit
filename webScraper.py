from bs4 import BeautifulSoup
import requests

keyWords = ["abortion", "crime+crime rates", "millitary spending+defense spending", "education", "gun violence+gun control", "healthcare+medicare", "imagration", "national security"]

def scrapeLinks():
    for i in keyWords:
        url = f"https://www.presidency.ucsb.edu/advanced-search?field-keywords=&field-keywords2={i}&field-keywords3=&from%5Bdate%5D=&to%5Bdate%5D=&person2=200320&category2%5B%5D=74&category2%5B%5D=73&category2%5B%5D=8&category2%5B%5D=52&category2%5B%5D=46&category2%5B%5D=48&category2%5B%5D=45&category2%5B%5D=65&category2%5B%5D=64&category2%5B%5D=49&items_per_page=100"
        print(url)
        response = requests.get(url)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        tr_tags = soup.find_all('tr', {'class': ['even', 'odd']})
    
    links = []
    for tr in tr_tags:
        td_title = tr.find('td', class_='views-field views-field-title')
        if td_title:
            link = td_title.a.get('href')
            if link:
                links.append(link)
    
    return links

# Execute the function
result = scrapeLinks()
print(result)