from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

genre = input('Enter Genre: ')
link = 'https://www.imdb.com/search/title?genres={}&countries=in&sort=year,asc&count=00&title_type=feature&release_date=2010,2018-12-31&runtime=1,1000'.format('genre')
response = requests.get(link)
soup = BeautifulSoup(response.text, "html.parser")


tagMOVIE = soup.find_all('span',class_ = 'userRatingValue')
tagMOVIE_list = []
for x in tagMOVIE:
    z = str(x)
    text = z[43:52]
    tagMOVIE_list.append(text)

nameMOVIE = soup.find_all('img',class_ = 'loadlate')
movie = []
for x in nameMOVIE:
    e = str(x)
    z = e.replace(',','.')
    y = z.find('class')
    nameOfMovie = z[10 : y - 2]
    movie.append(nameOfMovie)

timeTAG = soup.find_all('span', class_ = 'runtime')
time = []
for x in timeTAG:
    t = str(x.text[:-4])
    z = int(t)
    time.append(z)

yearTAG = soup.find_all('span', class_= 'lister-item-year text-muted unbold')
year = []
for x in yearTAG:
    z = str(x.text)
    a = re.findall(r'\d+', z)
    year.append(a[0])

print(movie)
print(time)
print(year)


