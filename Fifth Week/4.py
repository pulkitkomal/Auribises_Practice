# from scipy import stats
#
# x = [1,2,3,4,5]
# y = [2,4,5,4,5]
#
# data = stats.linregress
# print(data[0])
# print(data[1])

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
data = pd.read_csv("ad.csv")

x = data["TV"].values
y = data["Sales"].values


data = stats.linregress(x,y)
b1 = data[0]
b2 = data[1]

print(b1)
print(b2)

y1 = []

for X in x:
    Y = b1 + (b1*X)
    y1.append(Y)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.plot(x,y,"o",x,y1)
plt.show()

