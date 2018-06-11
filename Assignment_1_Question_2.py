a = []
b = int(input('Number of values: '))
for x in range(0, b):
    i = int(input('Enter Element: '))
    a.append(i)

print('Original Value:', a)
print('Right Shift by 3: ', a[-3 % len(a):] + a[:-3 % len(a)])