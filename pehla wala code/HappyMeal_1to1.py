class McDonalds:
    def __init__(self, name, order):
        self.name = name
        self.order = order

    def showOrder(self):
        print('Hi', self.name)
        self.order.show()


class Order:
    def __init__(self, burger, fries, coke, toy):
        self.burger = burger
        self.fries = fries
        self.coke = coke
        self.toy = toy

    def show(self):
        print('Your Order is a {} burger, {} fries, a {} coke & a {} for the child. Please wait a few minutes.'
              .format(self.burger, self.fries, self.coke, self.toy))


i1 = input('Your Name? ')
i2 = input('What kind of burger would you like? ')
i3 = input('Small or Large Fries? ')
i4 = input('Medium or Large coke?  ')
i5 = input('Is it for a Boy or a Girl? ')
if i5 == 'boy':
    i5 = 'HotWheel'
elif i5 == 'Boy':
    i5 = 'HotWheel'
elif i5 == 'girl':
    i5 = 'Barbie'
elif i5 == 'Girl':
    i5 = 'Barbie'
else:
    i5 = 'no valid input given'
o1 = Order(i2, i3, i4, i5)
m1 = McDonalds(i1, o1)
m1.showOrder()

