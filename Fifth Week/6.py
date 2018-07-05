import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


response = requests.get("https://gaana.com/artist/marshmello")
soup = BeautifulSoup(response.text,"html.parser")
#print(soup.prettify())
titlelist = []
durList = []





tdTags = soup.find_all('span', class_="parentnode sourcelist_1256640")
for tag in tdTags:
    #print(tag.text)
    result = re.findall(r"\w+", tag.text)
    y = result.index('title')
    x = result.index('id')
    u = result[y + 1:x]
    title = ' '.join(u)
    titlelist.append(title)

    #print('-----------')
    z = result.index('duration')

    dur = result[z+1]
    s=int(dur)
    durList.append(s)
    #print(dur)

    #print(title)
dataset = list(zip(titlelist,durList))
df = pd.DataFrame(data=dataset,columns=["title","duration"])
df.to_csv("abc.csv",index=False,header=True)
print(titlelist)
print(durList)

plt.bar(titlelist, durList, label="Duration", width=0.5)

plt.legend()

plt.xlabel("Title")
plt.ylabel("Duration")

plt.title("Data")

plt.show()