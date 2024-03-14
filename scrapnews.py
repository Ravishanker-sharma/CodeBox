import requests
from bs4 import BeautifulSoup

Url="https://www.hindustantimes.com/world-news"

headerss = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}
web = requests.get(Url,headers=headerss)

while True:
    if str(web) == "<Response [200]>":
        print(web)
        soup = BeautifulSoup(web.content,'html.parser')
        newses = soup.find('h2',class_="hdg3")
        print(newses)
        news = newses.find('a')['href']
        Url2 = f"https://www.hindustantimes.com{news}"
        new_web = requests.get(Url2,headers=headerss)
        new_soup = BeautifulSoup(new_web.content,'html.parser')
        heading = (new_soup.find('h1',class_='hdg1')).text
        detail = new_soup.find('h2',class_='sortDec').text
        picture = new_soup.find('div',class_='storyParagraphFigure').find('picture').find('img')['src']
        print(heading)
        print(detail)
        print(picture)
        break
    else:
        print(web)
