import random
counter = 0
tries = 0
won = 0
lost = 0
print('Total Number of Tries Given are 5')
while counter <= 5:
    a = random.randint(2, 9)
    n = a+2
    m = a-2
    i = input('Guess Number between 0 and 9: ')
    x = int(i)
    if x == a:
        print('You are right')
        counter += 1
        won += 1
    elif x > m and x < n:
        print('You were close')
        counter += 1
        tries += 1
    else:
        print('You are wrong')
        counter += 1
        lost += 1
    if counter == 5:
        print('Won: ', won)
        print('Tries: ', tries)
        print('Lost: ', lost)
