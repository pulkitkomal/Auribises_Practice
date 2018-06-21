class Order:
    def __init__(self, order):
        self.order = order

    def show(self):
        print('{}'.format(self.order))


class Address:
    def __init__(self, address):
        self.address = address

    def show(self):
        print('The Address you have entered is: ', self.address)


class Amazon:
    def __init__(self, name, order, address):
        self.name = name
        self.order = order
        self.address = address

    def show(self):
        print('Today you have ordered: ')
        for o in orderList:
            o.show()
        self.address.show()


class Seller(Amazon):
    def __init__(self, sellerName, name, order, address):
        super().__init__(name, order, address)
        self.sellerName = sellerName

    def show(self):
        print('----------------------------------')
        print('Hello', self.name)
        print('This is', self.sellerName)
        print('Your invoice follows: ')
        super().show()
        print('Your Order will arrive in a few days. Thank you for shopping with us.')


a1 = input('What is your name? ')
o1 = int(input('How many items would you like to order today? '))
orderList = []
for x in range(0, o1):
    z = input('Please enter your {} order: '.format(x+1))
    orderList.append(Order(z))
ad1 = input('What is your Address? ')
ad = Address(ad1)
seller = 'ABC Enterprises'
s = Seller(seller, a1, orderList, ad)
s.show()
