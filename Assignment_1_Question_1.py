a = ['mile', 'xylo', 'apple', 'xavier', 'aar', 'xiar']
a.sort()
c = []
z = 0
for x in range(0, len(a)):
    b = a[x]
    if b[0:1] == 'x':
        c.append(b)
d = c + a
v = []
for y in d:
    if y not in v:
        v.append(y)

print(v)
