import requests
from tkinter import *

url = " https://api.openweathermap.org/data/2.5/weather?id=1264728&APPID=62193150d24ac8c12795fb6174c55eb1"

reponse = requests.get(url)


json = reponse.json()
a = ' '
weather = json["weather"]
for x in range(0,len(weather)):
    print(weather[x])

main = json["main"]
print(main)

temp = main['temp']
print(temp-273.15,'C')


root = Tk()
root.title("Weather App Ludhiana")

weatherLabel = Label