import math
import random
a = (1,1)
b = (1,0)
c = (0,2)
d = (2,4)
e = (3,5)
lis = [a,b,c,d,e]
v = random.choice(lis)
u = random.choice(lis)
while u == v:
    u = random.choice(lis)
# print(u)
def dist(x, y):
    result = ((x[0]-y[0])*(x[0]-y[0]))+((x[1]-y[1])*(x[1]-y[1]))
    return math.sqrt(result)

l1 = []
l2 = []
for x in lis:
    l1.append(dist(x,u))
    l2.append(dist(x,v))
print(l1)
print(l2)

c1 = []
c2 = []
for x in range(0,5):
    if(l1[x]<l2[x]):
       c1.append(x)
    else:
        c2.append(x)
sum = 0
sum1 = 0
for x in c1:
    sum = sum+lis[x][0]
    sum1 = sum1 + lis[x][1]
print('----------------')
sum = sum/len(c1)
sum1 = sum/len(c1)
nc1 = [sum,sum1]
print(nc1)
for x in c2:
    sum = sum+lis[x][0]
    sum1 = sum1 + lis[x][1]
print('----------------')
sum = sum/len(c2)
sum1 = sum/len(c2)
nc2 = [sum,sum1]
print(nc2)
