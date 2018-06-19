'''
s = "and by and"

words = s.split()
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1

print(counts)
'''

file = open("Amazon_1toMany.py", "r")

data = file.read()

words = data.split()
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1


for x in counts:
    if x == 'class':
        print('Number of CLasses made:', counts[x])
    if x == 'def':
        print('Number of Methods made:', counts[x])
    if x == '__init__(self,':
        print('Number of __init__ constructor made:', counts[x])
    if x == 'for':
        print('Number of for loops used:', counts[x])


