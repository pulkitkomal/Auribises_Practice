from bs4 import BeautifulSoup
import requests
from urlextract import URLExtract

# search = input('Input: ')

# searchAMAZON = search.replace(" ", "+")
URL = 'https://www.1mg.com/search/all?name=glycomet'
response = requests.get(URL)
print(URL)
soup = BeautifulSoup(response.text,"html.parser")
print(soup)

