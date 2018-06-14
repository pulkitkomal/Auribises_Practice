class DB:
    totalAmt = []
    def __init__(self, name):
        self.name = name

    def getDB(self):
        db1 = input('Please Enter your name: ')
        self.name = db1

    def showDB(self):
        print('Hello', self.name)

d = DB(' ')
d.getDB()
d.showDB()