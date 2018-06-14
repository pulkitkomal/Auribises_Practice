from McDonalds_Recipt import DB_obj as obj
import random

class mcdonalds:

    def __init__(self, name, burgers, sides, beverages, deserts, meals, slipnumber):
        self.name = name
        self.burgers = burgers
        self.sides = sides
        self.beverages = beverages
        self.deserts = deserts
        self.meals = meals
        self.slipnumber = slipnumber

    def getData(self):
        self.name.getDB()
        get = input('Would you Buy a meal or Order separately? Press 1 or 2 ')
        if get == '1':
            self.meals.getMealData()
        else:
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
        self.meals.showMealData()
        self.burgers.showBurgerData()
        self.sides.showSidesData()
        self.beverages.showBevData()
        self.deserts.showDesData()
        print('Total amount is Rs.', sum(obj.db.totalAmt))
        print('Have a nice day')


slip = random.randint(1111, 9999)


mc = mcdonalds(obj.db, obj.bu, obj.s, obj.b, obj.d, obj.me, slip)
mc.getData()
mc.showData()