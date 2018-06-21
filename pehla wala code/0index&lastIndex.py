y = []

def in_list():
    u = int(input('Enter total elements: '))

    for x in range(0, u):
        i = input('Enter element to be stored: ')
        y.append(i)
    print(y)

def loc():
    print('The Value at index 0 is ', y[0])
    z = len(y)
    print('The Value at last index is ', y[z-1])

in_list()
loc()
