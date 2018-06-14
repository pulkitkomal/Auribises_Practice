from McDonalds_Recipt import a_first

class sides:

    def __init__(self, sidesName):
        self.sidesName = sidesName

    def getSidesData(self):
        b1 = input('Would you like to buy any Sides or Wraps? Enter 1 for Yes and 2 for No: ')
        if b1 == '1':
            b2 = input('''Which one would you like ? Please Enter the number from the list below.
    1. Veg Pizza McPuff
    2. French Fries (Small)
    3. French Fries (Medium)
    4. French Fries (Large)
    5. Spicy Paneer Wrap
    6. Grilled Chicken Wrap
    7. Spicy Chicken Wrap
    8. Chicken McNuggets (6 pc)
    9. Chicken McNuggets (9 pc)
    Press Enter 0 for None  ''')
            if b2 == '1':
                a_first.DB.totalAmt.append(60)
                self.sidesName = 'Veg Pizza McPuff - Rs.60'
            elif b2 == '2':
                a_first.DB.totalAmt.append(30)
                self.sidesName = 'French Fries (Small) - Rs.30'
            elif b2 == '3':
                a_first.DB.totalAmt.append(50)
                self.sidesName = 'French Fries (Medium)- Rs.50'
            elif b2 == '4':
                a_first.DB.totalAmt.append(70)
                self.sidesName = 'French Fries (Large) - Rs.70'
            elif b2 == '5':
                a_first.DB.totalAmt.append(70)
                self.sidesName = 'Spicy Paneer Wrap - Rs.70'
            elif b2 == '6':
                a_first.DB.totalAmt.append(90)
                self.sidesName = 'Grilled Chicken Wrap - Rs.90'
            elif b2 == '7':
                a_first.DB.totalAmt.append(100)
                self.sidesName = 'Spicy Chicken Wrap - Rs.100'
            elif b2 == '8':
                a_first.DB.totalAmt.append(70)
                self.sidesName = 'Chicken McNuggets (6 pc) - Rs.70'
            elif b2 == '9':
                a_first.DB.totalAmt.append(120)
                self.sidesName = 'Chicken McNuggets (9 pc) - Rs.120'
            else:
                print('No Valid input given. ')
                pass
        elif b1 == '2':
            pass
        else:
            print('No valid input given')
            exit()

    def showSidesData(self):
        print(self.sidesName)
        print(a_first.DB.totalAmt)

