from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
co = input('Enter Country Name: ')
year = []
rate = []
for x in range(0,10):
    a = input('Year: ')
    b = input('Rate: ')
    c = float(b)
    year.append(a)
    rate.append(c)

dataset = list(zip(year,rate))
df = pd.DataFrame(data=dataset,columns=["year","rate"])
df.to_csv("unemploy{}.csv".format(co),index=False,header=True)
print(year)
print(rate)
 # data = pd.read_csv("dataGDP.csv")
# Y = data["share"].values
# X = data["country"].values
# plt.bar(X, Y, label="GDP Share", width=0.5)
#
# plt.legend()
# plt.xlabel("Country")
# plt.ylabel("Share")
# plt.title("GDP Data")
# plt.show()