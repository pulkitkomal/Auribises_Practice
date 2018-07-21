import pandas as pd
from difflib import SequenceMatcher


df = pd.read_csv('players.csv')
z = input('Enter name of player: ')

for x in range(len(df['Name'])):
    a = df['Name'][x]
    v = a.replace('*', ' ')
    ratio = SequenceMatcher(None, v, z).ratio()
    if ratio >= 0.5:
        print('Name: ',df['Name'][x])
        print('Total number of matches played in Test',df['TestM'][x])
        print('Total runs in Test',df['TestRuns'][x])
        print('Bat avg in Test',df['TestBat Avg'][x])
        print('Wickets in Test',df['TestWkts'][x])
        print('Bowl avg in Test',df['TestBowl Avg'][x])

        print('Total number of matches played in ODI',df['ODIM'][x])
        print('Total runs in ODI',df['ODIRuns'][x])
        print('Bat avg in ODI',df['ODIBat Avg'][x])
        print('Wickets in ODI',df['ODIWkts'][x])
        print('Bowl avg in ODI',df['ODIBowl Avg'][x])

        print('Total number of matches played in T20',df['T20M'][x])
        print('Total runs in T20',df['T20Runs'][x])
        print('Bat avg in T20',df['T20Bat Avg'][x])
        print('Wickets in T20',df['T20Wkts'][x])
        print('Bowl avg in T20',df['T20Bowl Avg'][x])