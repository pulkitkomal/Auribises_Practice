from tkinter import *
import threading
import requests


def run1():
    startLAT = startLAT_EN.get()
    startLONG = startLONG_EN.get()
    endLAT = endLAT_EN.get()
    endLONG = endLONG_EN.get()

    url = "https://api.uber.com/v1.2/estimates/price?start_latitude={}&start_longitude={}&end_latitude={}&end_longitude={}".format(
            startLAT, startLONG, endLAT, endLONG)
    header = {'Authorization': 'Token VoyrYWbfzAVKNjjFOtUBoSmbJMkzLj1flztpJD7P', 'Accept-Language': 'en_US',
                  'Content-Type': 'application/json'}
    response = requests.get(url, headers=header)

    json = response.json()
    price = json["prices"]

    priceGoLow = ' '
    priceGoHigh = ' '

    priceMOTOLow = ' '
    priceMOTOHigh = ' '

    priceXLow = ' '
    priceXHigh = ' '

    for x in range(0, len(price)):

        if price[x]['localized_display_name'] == 'UberGo':
            priceGoHigh = price[x]['high_estimate']
            priceGoLow = price[x]['low_estimate']
        elif price[x]['localized_display_name'] == 'MOTO':
            priceMOTOHigh = price[x]['high_estimate']
            priceMOTOLow = price[x]['low_estimate']
        elif price[x]['localized_display_name'] == 'X':
            priceXHigh = price[x]['high_estimate']
            priceXLow = price[x]['low_estimate']

    print('Go', priceGoLow)
    print('Go', priceGoHigh)
    print('MOTO', priceMOTOLow)
    print('MOTO', priceMOTOHigh)
    print('X', priceXLow)
    print('X', priceXHigh)


root = Tk()

root.title('Uber Fare Estimate')
startLAT = Label(root, text='Enter Start Latitude ').grid(row=0, column=0)
startLAT_EN = Entry(root)
startLAT_EN.grid(row=0, column=10)

startLONG = Label(root, text='Enter Start Longitude ').grid(row=10, column=0)
startLONG_EN = Entry(root)
startLONG_EN.grid(row=10, column=10)

space0 = Label(root, text='           ').grid(row=20, column=0)

endLAT = Label(root, text='Enter End Latitude ').grid(row=30, column=0)
endLAT_EN = Entry(root)
endLAT_EN.grid(row=30, column=10)

endLONG = Label(root, text='Enter End Longitude ').grid(row=40, column=0)
endLONG_EN = Entry(root)
endLONG_EN.grid(row=40, column=10)

space1 = Label(root, text='           ').grid(row=50, column=0)

btn = Button(root, text='Submit', command=run1).grid(row=60, column=5)

space3 = Label(root, text='           ').grid(row=70, column=0)


root.resizable(False, False)
root.mainloop()