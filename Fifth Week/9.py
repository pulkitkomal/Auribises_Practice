import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


response = requests.get("https://gaana.com/artist/marshmello")
soup = BeautifulSoup(response.text,"html.parser")

durList = []

tdTags = soup.find_all('span', class_="parentnode sourcelist_1256640")
for tag in tdTags:

    result = re.findall(r"\w+", tag.text)
    z = result.index('duration')
    dur = result[z+1]
    s=int(dur)
    durList.append(s)

response = requests.get('https://gaana.com/artist/arijit-singh')
soup = BeautifulSoup(response.text,"html.parser")

durListAJ = []

CHTags = soup.find_all('span', class_="parentnode sourcelist_52767")
for tag in CHTags:

    result = re.findall(r"\w+", tag.text)
    z = result.index('duration')
    dur = result[z+1]
    s=int(dur)
    durListAJ.append(s)



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
plt.plot(X, Y, "o", X, Y1)
plt.show()