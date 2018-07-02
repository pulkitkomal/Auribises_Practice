import pandas as pd
import matplotlib.pyplot as plot

df = pd.read_csv('SalesJan2009.csv')
print(df)
c = df['Product'].value_counts()
print(c)