from McDonalds_Recipt import DB_obj as obj
import random

class mcdonalds:

    def __init__(self, name, burgers, sides, beverages, deserts, slipnumber):
        self.name = name
        self.burgers = burgers
        self.sides = sides
        self.beverages = beverages
        self.deserts = deserts
        self.slipnumber = slipnumber

    def getData(self):
        self.name.getDB()
        self.burgers.getBurgerData()
        self.sides.getSidesData()
        self.beverages.getBevData()
        self.deserts.getDesData()

    def showData(self):
        print('-----------------------------------------')
        self.name.showDB()
        print('The Receipt of your Order follows: ')
        print('Order Number is', self.slipnumber)
        print('You have ordered: ')
        self.burgers.showBurgerData()
        self.sides.showSidesData()
        self.beverages.showBevData()
        self.deserts.showDesData()
        print('Total amount is Rs.', sum(obj.db.totalAmt))
        print('Have a nice day')


slip = random.randint(1111, 9999)


mc = mcdonalds(obj.db, obj.bu, obj.s, obj.b, obj.d, slip)
mc.getData()
mc.showData()