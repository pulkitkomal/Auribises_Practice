class McDonalds:
    def __init__(self, name, order):
        self.name = name
        self.order = order

    def showOrder(self):
        print('Hi', self.name)
        self.order.show()


class Order:
    def __init__(self, burger, fries, coke):
        self.burger = burger
        self.fries = fries
        self.coke = coke


    def show(self):
        print('Your Order is a {} burger, {} fries & a {} coke. Please wait a few minutes.'
              .format(self.burger, self.fries, self.coke))


i1 = input('Your Name? ')
i2 = input('What kind of burger would you like? ')
i3 = input('Small or Large Fries? ')
i4 = input('Medium or Large coke?  ')
o1 = Order(i2, i3, i4)
m1 = McDonalds(i1, o1)
m1.showOrder()

