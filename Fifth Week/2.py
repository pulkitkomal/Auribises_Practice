import pandas as pd

df = pd.read_csv('Banglore.csv')

print(df)
print(df.head())
print(df.head(10))
print(df.tail())
print(df.tail(10))

print('---------------')
print(df.shape)
print(df.iloc[0:5, 0:4])
print('---------------')

print(df.loc[100:200,["Temperature","Humidity"]])

print('---------------')

print(df["Temperature"])
