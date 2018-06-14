from McDonalds_Recipt import a_first

class beverages:

    def __init__(self, bevName):
        self.bevName = bevName

    def getBevData(self):
        b1 = input('Would you like to buy any Beverages? Enter 1 for Yes and 2 for No: ')
        if b1 == '1':
            b2 = input('''Which one would you like ? Please Enter the number from the list below.
    1. McFloat (Coke)
    2. McFloat (Fanta)
    3. McFloat (Sprite)
    4. Coke (Small)
    5. Coke (Medium)
    6. Coke (Large)
    7. Sprite (Small)
    8. Sprite (Medium)
    9. Sprite (Large)
    Press Enter 0 for None  ''')
            if b2 == '1':
                a_first.DB.totalAmt.append(70)
                self.bevName = 'McFloat (Coke) - Rs.70'
            elif b2 == '2':
                a_first.DB.totalAmt.append(70)
                self.bevName = 'McFloat (Fanta) - Rs.70'
            elif b2 == '3':
                a_first.DB.totalAmt.append(70)
                self.bevName = 'McFloat (Sprite)- Rs.70'
            elif b2 == '4':
                a_first.DB.totalAmt.append(40)
                self.bevName = 'Coke (Small) - Rs.40'
            elif b2 == '5':
                a_first.DB.totalAmt.append(60)
                self.bevName = 'Coke (Medium) - Rs.60'
            elif b2 == '6':
                a_first.DB.totalAmt.append(90)
                self.bevName = 'Coke (Large) - Rs.90'
            elif b2 == '7':
                a_first.DB.totalAmt.append(40)
                self.bevName = 'Sprite (Small) - Rs.40'
            elif b2 == '8':
                a_first.DB.totalAmt.append(60)
                self.bevName = 'Sprite (Medium) (6 pc) - Rs.60'
            elif b2 == '9':
                a_first.DB.totalAmt.append(90)
                self.bevName = 'Sprite (Large) (9 pc) - Rs.90'
            else:
                print('No Valid input given. ')
                pass
        elif b1 == '2':
            pass
        else:
            print('No valid input given')
            exit()

    def showSidesData(self):
        print(self.bevName)
        print(a_first.DB.totalAmt)

b = beverages(' ')
b.getBevData()
b.showSidesData()