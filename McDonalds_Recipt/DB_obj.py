from McDonalds_Recipt import a_first, DB_Burgers, DB_Sides, DB_Beverages, Deserts

db = a_first.DB(' ')
db.getDB()
db.showDB()

bu = DB_Burgers.Burgers(' ')
bu.getBurgerData()
bu.showBurgerData()

s = DB_Sides.sides(' ')
s.getSidesData()
s.showSidesData()

b = DB_Beverages.beverages(' ')
b.getBevData()
b.showBevData()

d = Deserts.deserts(' ')
d.getDesData()
d.showDesData()