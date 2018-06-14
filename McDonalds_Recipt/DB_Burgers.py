from McDonalds_Recipt import a_first


class Burgers:

    def __init__(self, burgerName):
        self.burgerName = burgerName

    def getBurgerData(self):
        b1 = input('Would you like to buy a burger? Enter 1 for Yes and 2 for No: ')
        if b1 == '1':
            b2 = input('''Which burger would you like to eat? Please Enter the number from the list below.
    1. McAloo Tikki
    2. McVeggie
    3. McSpicy Paneer
    4. McEgg
    5. Chicken McGrill
    6. McChicken
    7. Filet-O-Fish
    8. McSpicy Chicken
    9. Veg Maharaja Mac
    10. Chicken Maharaja Mac
Press Enter 0 for None  ''')
            if b2 == '1':
                a_first.DB.totalAmt.append(30)
                self.burgerName = 'McAloo Tikki - Rs.30'
            elif b2 == '2':
                a_first.DB.totalAmt.append(40)
                self.burgerName = 'McVeggie - Rs.40'
            elif b2 == '3':
                a_first.DB.totalAmt.append(60)
                self.burgerName = 'McSpicy Paneer - Rs.60'
            elif b2 == '4':
                a_first.DB.totalAmt.append(50)
                self.burgerName = 'McEgg - Rs.50'
            elif b2 == '5':
                a_first.DB.totalAmt.append(80)
                self.burgerName = 'Chicken McGrill - Rs.80'
            elif b2 == '6':
                a_first.DB.totalAmt.append(100)
                self.burgerName = 'McChicken - Rs.100'
            elif b2 == '7':
                a_first.DB.totalAmt.append(120)
                self.burgerName = 'Filet-O-Fish - Rs.120'
            elif b2 == '8':
                a_first.DB.totalAmt.append(90)
                self.burgerName = 'McSpicy Chicken - Rs.90'
            elif b2 == '9':
                a_first.DB.totalAmt.append(170)
                self.burgerName = 'Veg Maharaja Mac - Rs.170'
            elif b2 == '10':
                a_first.DB.totalAmt.append(220)
                self.burgerName = 'Chicken Maharaja Mac - Rs.220'
            else:
                print('No Valid input given. ')
                pass
        elif b1 == '2':
            pass
        else:
            print('No valid input given')
            exit()

    def showBurgerData(self):
        print(self.burgerName)



