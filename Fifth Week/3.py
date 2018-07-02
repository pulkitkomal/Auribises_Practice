import pandas as pd

s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series(['John', 'Jonnie', 'Jim', 'Jack', 'Joe'])

print(type(s1))
print(s1)
print('------')
print(s2)
print('------')

df = pd.DataFrame([s1,s2])
print(df)

df = pd.DataFrame(
    [
        [101,102],
        ["john","Jennie"]
    ],
    index=['R1', 'R2'],
    columns=['C1', 'C2']
)
print('------')

print(df)

print(df.loc["Roll Number":"Name", "C1"])

df = pd.DataFrame(
    {
        'roll':[101,102,103],
        'name':['John','Sia','Mike']
    }
)
print('------')

print(df)
print('------')

print(df['roll'])

df1 = df['roll'] > 102
print(df1)
