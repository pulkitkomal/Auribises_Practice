from McDonalds_Recipt import a_first


class deserts:

    def __init__(self, desName):
        self.desName = desName

    def getDesData(self):
        b1 = input('Would you like to buy any Deserts? Enter 1 for Yes and 2 for No: ')
        if b1 == '1':
            b2 = input('''Which one would you like ? Please Enter the number from the list below.
    1. Soft Serve Cone
    2. McSwril Chocolate
    3. McSwril Butterscotch
    4. Soft Serve Chocolate
    5. Soft Serve Strawberry
    Press Enter 0 for None  ''')
            if b2 == '1':
                a_first.DB.totalAmt.append(20)
                self.desName = 'Soft Serve Cone - Rs.20'
            elif b2 == '2':
                a_first.DB.totalAmt.append(30)
                self.desName = 'McSwril Chocolate - Rs.30'
            elif b2 == '3':
                a_first.DB.totalAmt.append(35)
                self.desName = 'McSwril Butterscotch- Rs.35'
            elif b2 == '4':
                a_first.DB.totalAmt.append(30)
                self.desName = 'Soft Serve Chocolate - Rs.30'
            elif b2 == '5':
                a_first.DB.totalAmt.append(30)
                self.desName = 'Soft Serve Strawberry - Rs.30'
            else:
                print('No Valid input given. ')
                pass
        elif b1 == '2':
            pass
        else:
            print('No valid input given')
            exit()

    def showDesData(self):
        print(self.desName)




