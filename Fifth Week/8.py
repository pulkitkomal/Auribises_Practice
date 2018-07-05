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
    # print(title)
    # print(dur)

response = requests.get('https://gaana.com/artist/arijit-singh')
soup = BeautifulSoup(response.text,"html.parser")
#print(soup.prettify())
titlelistAJ = []
durListAJ = []

CHTags = soup.find_all('span', class_="parentnode sourcelist_52767")
for tag in CHTags:
    #print(tag.text)
    result = re.findall(r"\w+", tag.text)
    y = result.index('title')
    x = result.index('id')
    u = result[y + 1:x]
    title = ' '.join(u)
    titlelistAJ.append(title)
    # print('-----------')
    z = result.index('duration')
    dur = result[z+1]
    s=int(dur)
    durListAJ.append(s)
    # print(title)
    # print(dur)

# print(durList)
# print(durListAJ)


dataset = list(zip(durList,durListAJ))
df = pd.DataFrame(data=dataset,columns=["Marshmello","Arijit Singh"])
df.to_csv("maj.csv",index=False,header=True)

data = pd.read_csv("maj.csv")

X = data["Marshmello"].values
Y = data["Arijit Singh"].values

data = stats.linregress(X,Y)
b1 = data[0]
b0 = data[1]

print("b1 is",b1)
print("b0 is",b0)

Y1 = []

for x in X:
    y = b0 + (b1*x)
    Y1.append(y)

print("============")
print(Y1)
print("============")

plt.xlabel('Marshmello')
plt.ylabel('Arijit Singh')
plt.grid(True)
# plt.plot(X, Y, "ro")
plt.plot(X, Y, "o", X, Y1)
plt.show()