import requests
import sys
from bs4 import BeautifulSoup
r = requests.get('https://www.flipkart.com/search?q=laptop')
content = r.content.decode(encoding='UTF-8')
soup = BeautifulSoup(r.content.decode(encoding='UTF-8'), "lxml")
reviews = soup.find_all('div', {"class": "_3wU53n"})
for item in reviews:
    print(item.text)