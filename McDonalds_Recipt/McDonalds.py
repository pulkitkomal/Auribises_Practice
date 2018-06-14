from McDonalds_Recipt import DB_obj as obj


class mcdonalds:

    def __init__(self, name, burgers, sides, beverages, deserts):
        self.name = name
        self.burgers = burgers
        self.sides = sides
        self.beverages = beverages
        self.deserts = deserts

    def getData(self):
        self.name.getDB()
        self.burgers.getBurgerData()
        self.sides.getSidesData()
        self.beverages.getBevData()
        self.deserts.getDesData()

    def showData(self):
        self.name.showDB()
        self.burgers.showBurgerData()
        self.sides.showSidesData()
        self.beverages.showBevData()
        self.deserts.showDesData()


mc = mcdonalds(obj.db, obj.bu, obj.s, obj.b, obj.d)
mc.getData()
mc.showData()