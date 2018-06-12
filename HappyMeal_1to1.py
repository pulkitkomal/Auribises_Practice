class McDonalds:
    def __init__(self, order):
        self.order = order

    def showOrder(self):
        self.order.show()


class Order:
    def __init__(self, name, burger, fries, coke ):
        self.name = name
        self.burger = burger
        self.fries = fries
        self.coke = coke


    def show(self):
        print('Your Order is a {} burger, {} fries & {} coke for {} '.format(self.burger,
                                                                           self.fries,
                                                                           self.coke,
                                                                           self.name))


i1 = input('Your Name? ')
i2 = input('Aloo Tikki or McChicken Burger? ')
i3 = input('Small or Large Fries? ')
i4 = input('Medium or Large coke?  ')
o1 = Order(i1, i2, i3, i4)
m1 = McDonalds(o1)
m1.showOrder()

