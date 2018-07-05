import requests
from bs4 import BeautifulSoup
import re


response = requests.get("https://gaana.com/artist/marshmello")
soup = BeautifulSoup(response.text,"html.parser")

#print(soup.prettify())
titlelist = []
durList = []
tdTags = soup.find_all('span', class_="parentnode sourcelist_1256640")
for tag in tdTags:
    #print(tag.text)
    result = re.findall(r"\w+", tag.text)
    #print('-----------')
    z = result.index('duration')
    y = result.index('title')
    x = result.index('id')
    dur = result[z+1]
    durList.append(dur)
    #print(dur)
    u = result[y+1:x]
    title = ' '.join(u)
    titlelist.append(title)
    #print(title)

print(titlelist)
print(durList)

