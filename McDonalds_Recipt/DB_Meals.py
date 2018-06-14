from McDonalds_Recipt import a_first


class meals:

    def __init__(self, mealName):
        self.mealName = mealName

    def getMealData(self):
        b2 = input('''Which one would you like ? Please Enter the number from the list below.
    1. McAloo Tikki Meal
    2. Aloo Wrap Meal
    3. McEgg Meal
    4. Chicken McGrill Meal
    5. Grilled Chicken Wrap Meal
    Press Enter 0 for None  ''')
        if b2 == '1':
            a_first.DB.totalAmt.append(30)
            f = input('''Would you like your Meal with
    1.Medium Fries & Medium Coke
    2.Medium Fries & Large Coke
    3.Large Fries & Medium Coke
    4.Large Fries & Large Coke ''')
            if f == '1':
                a_first.DB.totalAmt.append(50)
                a_first.DB.totalAmt.append(60)
                self.mealName = 'McAloo Tikki - Rs.30\n'\
                                'French Fries (Medium)- Rs.50\n'\
                                'Coke (Medium) - Rs.60\n'
            elif f == '2':
                a_first.DB.totalAmt.append(50)
                a_first.DB.totalAmt.append(90)
                self.mealName = 'McAloo Tikki - Rs.30\n' \
                                'French Fries (Medium)- Rs.50\n' \
                                'Coke (Large) - Rs.90'
            elif f == '3':
                a_first.DB.totalAmt.append(70)
                a_first.DB.totalAmt.append(60)
                self.mealName = 'McAloo Tikki - Rs.30\n' \
                                'French Fries (Large)- Rs.70\n' \
                                'Coke (Medium) - Rs.60'
            elif f == '4':
                a_first.DB.totalAmt.append(70)
                a_first.DB.totalAmt.append(90)
                self.mealName = 'McAloo Tikki - Rs.30\n' \
                                'French Fries (Large)- Rs.70\n' \
                                'Coke (Large) - Rs.90'



        elif b2 == '2':
            a_first.DB.totalAmt.append(50)
            f = input('''Would you like your Meal with
    1.Medium Fries & Medium Coke
    2.Medium Fries & Large Coke
    3.Large Fries & Medium Coke
    4.Large Fries & Large Coke ''')
            if f == '1':
                a_first.DB.totalAmt.append(50)
                a_first.DB.totalAmt.append(60)
                self.mealName = '''McEgg - Rs.50
                                 French Fries (Medium)- Rs.50
                                 Coke (Medium) - Rs.60'''
            elif f == '2':
                a_first.DB.totalAmt.append(50)
                a_first.DB.totalAmt.append(90)
                self.mealName = 'McAloo Wrap - Rs.50\n' \
                                'French Fries (Medium)- Rs.50\n' \
                                'Coke (Large) - Rs.90'
            elif f == '3':
                a_first.DB.totalAmt.append(70)
                a_first.DB.totalAmt.append(60)
                self.mealName = 'McAloo Wrap - Rs.50\n' \
                                'French Fries (Large)- Rs.70\n' \
                                'Coke (Medium) - Rs.60'
            elif f == '4':
                a_first.DB.totalAmt.append(70)
                a_first.DB.totalAmt.append(90)
                self.mealName = 'McAloo Wrap - Rs.50\n' \
                                'French Fries (Large)- Rs.70\n' \
                                'Coke (Large) - Rs.90'
        elif b2 == '3':
            a_first.DB.totalAmt.append(50)
            f = input('''Would you like your Meal with
    1.Medium Fries & Medium Coke
    2.Medium Fries & Large Coke
    3.Large Fries & Medium Coke
    4.Large Fries & Large Coke ''')
            if f == '1':
                a_first.DB.totalAmt.append(50)
                a_first.DB.totalAmt.append(60)
                self.mealName = 'McEgg - Rs.50\n' \
                                'French Fries (Medium)- Rs.50\n' \
                                'Coke (Medium) - Rs.60'
            elif f == '2':
                a_first.DB.totalAmt.append(50)
                a_first.DB.totalAmt.append(90)
                self.mealName = 'McEgg - Rs.50\n' \
                                'French Fries (Medium)- Rs.50\n' \
                                'Coke (Large) - Rs.90'
            elif f == '3':
                a_first.DB.totalAmt.append(70)
                a_first.DB.totalAmt.append(60)
                self.mealName = 'McEgg - Rs.50\n' \
                                'French Fries (Large)- Rs.70\n' \
                                'Coke (Medium) - Rs.60'
            elif f == '4':
                a_first.DB.totalAmt.append(70)
                a_first.DB.totalAmt.append(90)
                self.mealName = 'McEgg - Rs.50\n' \
                                'French Fries (Large)- Rs.70\n' \
                                'Coke (Large) - Rs.90'
        elif b2 == '4':
            a_first.DB.totalAmt.append(80)
            f = input('''Would you like your Meal with
    1.Medium Fries & Medium Coke
    2.Medium Fries & Large Coke
    3.Large Fries & Medium Coke
    4.Large Fries & Large Coke ''')
            if f == '1':
                a_first.DB.totalAmt.append(50)
                a_first.DB.totalAmt.append(60)
                self.mealName = 'Chicken McGrill - Rs.80\n' \
                                'French Fries (Medium)- Rs.50\n' \
                                'Coke (Medium) - Rs.60'
            elif f == '2':
                a_first.DB.totalAmt.append(50)
                a_first.DB.totalAmt.append(90)
                self.mealName = 'Chicken McGrill - Rs.80\n' \
                                'French Fries (Medium)- Rs.50\n' \
                                'Coke (Large) - Rs.90'
            elif f == '3':
                a_first.DB.totalAmt.append(70)
                a_first.DB.totalAmt.append(60)
                self.mealName = 'Chicken McGrill - Rs.80\n' \
                                'French Fries (Large)- Rs.70\n' \
                                'Coke (Medium) - Rs.60'
            elif f == '4':
                a_first.DB.totalAmt.append(70)
                a_first.DB.totalAmt.append(90)
                self.mealName = 'Chicken McGrill - Rs.80\n' \
                                'French Fries (Large)- Rs.70\n' \
                                'Coke (Large) - Rs.90'
        elif b2 == '5':
            a_first.DB.totalAmt.append(90)
            f = input('''Would you like your Meal with
    1.Medium Fries & Medium Coke
    2.Medium Fries & Large Coke
    3.Large Fries & Medium Coke
    4.Large Fries & Large Coke ''')
            if f == '1':
                a_first.DB.totalAmt.append(50)
                a_first.DB.totalAmt.append(60)
                self.mealName = 'Grilled Chicken Wrap - Rs.90\n' \
                                'French Fries (Medium)- Rs.50\n' \
                                'Coke (Medium) - Rs.60'
            elif f == '2':
                a_first.DB.totalAmt.append(50)
                a_first.DB.totalAmt.append(90)
                self.mealName = 'Grilled Chicken Wrap - Rs.90\n' \
                                'French Fries (Medium)- Rs.50\n' \
                                'Coke (Large) - Rs.90'
            elif f == '3':
                a_first.DB.totalAmt.append(70)
                a_first.DB.totalAmt.append(60)
                self.mealName = 'Grilled Chicken Wrap - Rs.90\n' \
                                'French Fries (Large)- Rs.70\n' \
                                'Coke (Medium) - Rs.60'
            elif f == '4':
                a_first.DB.totalAmt.append(70)
                a_first.DB.totalAmt.append(90)
                self.mealName = 'Grilled Chicken Wrap - Rs.90\n' \
                                'French Fries (Large)- Rs.70\n' \
                                'Coke (Large) - Rs.90'
        else:
            print('No Valid input given. ')
            exit()

    def showMealData(self):
        print(self.mealName)
