from bs4 import BeautifulSoup
import requests


URL = 'https://gndec.ac.in/?q=latest_news'
response = requests.get(URL)

soup = BeautifulSoup(response.text,'html.parser')
tags = soup.find_all('li')
for x in tags:
    print(x)
