import requests
from bs4 import BeautifulSoup


response = requests.get("http://www.zomato.com/ludhiana/restaurants")
# print(response)
soup = BeautifulSoup(response.text,"html.parser")
print(soup.prettify())