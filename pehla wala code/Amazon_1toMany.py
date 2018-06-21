class Amazon:
    def __init__(self, name, order):
        self.name = name
        self.order = order

    def showOrder(self):
        print('Welcome ', self.name)
        print('Today you have ordered: ')
        for o in orderList:
            o.show()
        print('Your order will be arriving in a few days.')


class Order:
    def __init__(self, order):
        self.order = order

    def show(self):
        print('{}'.format(self.order))


a1 = input('What is your name? ')
o1 = int(input('How many items would you like to order today? '))
orderList = []
for x in range(0, o1):
    z = input('Please enter your {} order: '.format(x+1))
    orderList.append(Order(z))

a = Amazon(a1, orderList)
a.showOrder()


