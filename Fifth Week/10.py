import requests
from bs4 import BeautifulSoup
import re

lnk = input('Enter Link: ')
link = lnk.replace(' ', '-')

response = requests.get("https://gaana.com/artist/{}".format(link))
soup = BeautifulSoup(response.text,"html.parser")


Tags = soup.find_all('body')
a = str(Tags)
result = re.findall(r"\w+", a)
z = result.index('parentnode')
sourceTAG = result[z+1]


durListAJ = []

CHTags = soup.find_all('span', class_="parentnode {}".format(sourceTAG))
for tag in CHTags:

    result = re.findall(r"\w+", tag.text)
    z = result.index('duration')
    dur = result[z+1]
    s=int(dur)
    durListAJ.append(s)

print(durListAJ)


