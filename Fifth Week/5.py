import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.saavn.com/s/artist/marshmello-songs/Eevs5FiVgus_")
soup = BeautifulSoup(response.text,"html.parser")

print(soup)
Tags = soup.find_all('h1')
print(Tags[0].text)
tdTags = soup.find_all('p', class_="ellip")
time = soup.findAll('span', class_='meta-year small')


for tag in tdTags:
    print(tag.text)