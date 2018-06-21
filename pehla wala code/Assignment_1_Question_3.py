y = 0
c = []
k = []
for x in range(0, 10):
    m = 4
    o = y + m % 10
    z = o
    y = z
    if y >= 10:
        y = y - 10
    c.append(y)
for i in range(0, len(c)):
        for x in range(i + 1, len(c)):
            if c[i] == c[x]:
               k.append(c[x])
print('The number of candies you ate: ', len(k))
