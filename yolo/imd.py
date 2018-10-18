from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

genre = input('Enter Genre: ')
link = 'https://www.imdb.com/search/title?genres={}&countries=in&sort=year,asc&count=1000&title_type=feature&release_date=,2018-12-31&runtime=1,1000'.format('genre')
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
    z = str(x)
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

dataset = list(zip(movie, time, year))
df = pd.DataFrame(data=dataset, columns=["Movie", "Time", "Year"])
df.to_csv("tempDATA.csv", index=False, header=True)

def plotGraph():
    data = pd.read_csv("tempDATA.csv")
    X = data["Year"].values
    Y = data["Time"].values

    data = stats.linregress(X,Y)
    b1 = data[0]
    b0 = data[1]

    Y1 = []

    for x in X:
        y = b0 + (b1*x)
        Y1.append(y)
    pv = Y1[len(Y1) - 1]
    plt.title('Next {} movies predicted time is {}'.format(genre,pv))
    plt.xlabel('Year')
    plt.ylabel('Time')
    plt.grid(True)
    plt.plot(X, Y, "o")
    plt.plot(X, Y1)
    plt.show()

plotGraph()
