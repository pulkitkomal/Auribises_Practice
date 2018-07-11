from bs4 import BeautifulSoup
import pandas as pd
import requests

co = input('Enter Country Name: ')
WByear = []
WBrate = []
response = requests.get('https://ycharts.com/indicators/france_youth_unemployment_rate')
soup = BeautifulSoup(response.text,"html.parser")

tdTags = soup.find_all('td', class_="col1")
for tag in tdTags:
    c = tag.text[-4:]
    WByear.append(c)

tdTags = soup.find_all('td', class_="col2")
for tag in tdTags:
    c = tag.text[17:21]
    # d = float(c)
    # print(d)
    WBrate.append(c)


year = WByear[0:18]
rate = WBrate[0:18]
print(year)
print(rate)

dataset = list(zip(year,rate))
df = pd.DataFrame(data=dataset,columns=["year","rate"])
df.to_csv("unemploy{}.csv".format(co),index=False,header=True)

