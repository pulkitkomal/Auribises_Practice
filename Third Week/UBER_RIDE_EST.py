import requests

startLAT = 30.9123
startLONG = 75.8055
endLAT = 30.8856
endLONG = 75.7882

url = "https://api.uber.com/v1.2/estimates/price?start_latitude={}&start_longitude={}&end_latitude={}&end_longitude={}".format(startLAT, startLONG, endLAT, endLONG)
header = {'Authorization': 'Token VoyrYWbfzAVKNjjFOtUBoSmbJMkzLj1flztpJD7P', 'Accept-Language': 'en_US', 'Content-Type': 'application/json'}
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