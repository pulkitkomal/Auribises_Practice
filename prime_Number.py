i = int(input('Enter Prime Number: '))
num = 0
if i == 1:
    print('not Prime')
elif i == 2:
    print('Prime')
elif i > 2:
    for x in range(2, (i//2)+1):
        if i % x == 0:
            num = 1
        else:
            num = 2
while num == 1:
    print('Not Prime')
    break
while num == 2:
    print('Prime Number')
    break
