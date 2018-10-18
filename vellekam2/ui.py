from python_prac import team1
from python_prac import team2

z = ['AFG', 'AUS', 'BAN', 'BER', 'CAN', 'EAF',
     'ENG', 'HOK', 'IND', 'IRE', 'KEN', 'NAM', 'NEP', 'NED', 'NZL', 'OMA',
     'PAK', 'PNG', 'SCO', 'SAF', 'SRL', 'UAE', 'USA', 'WIN', 'ZIM']
print(z)
team1.dataEXT()
team2.dataEXT()
team1.TEAM1()
team2.TEAM2()
print('Team 1')
for x in range(0,75):
    print(x, team1.team1PLAYER[x])
print('Team 2')
for x in range(0,75):
    print(x, team2.team2PLAYER[x])
team1Select = []
team2Select = []
# a = input('a: ')
for x in range(0,11):
    a = int(input('Enter Number team 1: '))
    z = team1.team1PLAYER[a]
    team1Select.append(z)

print(team1Select)

for x in range(0,11):
    a = int(input('Enter Number team 2: '))
    z = team2.team2PLAYER[a]
    team2Select.append(z)
print(team2Select)
TEAM1 = 0
TEAM2 = 0
for x in range(0,11):
    z = team1.team1PLAYER.index(team1Select[x])
    y = team2.team2PLAYER.index(team2Select[x])
    print(team1Select[x])
    print(team2Select[x])
    if team1.team1TestPoints[z] > team2.team2TestPoints[y]:
        print('Test Team 1')
        TEAM1 +=1
    else:
        print('Test Team 2')
        TEAM2 +=1
    if team1.team1ODIPoints[z] > team2.team2ODIPoints[y]:
        print('ODI Team 1')
        TEAM1 +=1

    else:
        print('ODI Team 2')
        TEAM2 +=1

    if team1.team1T20Points[z] > team2.team2T20Points[y]:
        print('T20 Team 1')
        TEAM1 +=1

    else:
        print('T20 Team 2')
        TEAM2 +=1

if TEAM1 > TEAM2:
    print('\nTeam 1 wins')
else:
    print('\nTeam 2 wins')