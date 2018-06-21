from tkinter import *

def onClick():
    Name = nameEN.get()
    Age = ageEN.get()
    gender = varGender.get()
    Country = varCountry.get()
    Email = emailEN.get()

    if gender == 'Male':
        gender = 'his'
    elif gender == 'Female':
        gender = 'her'

    print("{} belongs to {}, {} age is {}, you can contact her on {}".format(Name, Country, gender, Age, Email))


root = Tk()

title = Label(root, text='Enter your details below!!')
title.grid(row=10, column=10)

name = Label(root, text='Enter your name')
name.grid(row=20, column=10)

nameEN = Entry(root)
nameEN.grid(row=30, column=10)

age = Label(root, text='Enter your age')
age.grid(row=40, column=10)

ageEN = Entry(root)
ageEN.grid(row=50, column=10)

Gender = Label(root, text='Select your Gender below')
Gender.grid(row=60, column=10)

varGender = StringVar(root)
varGender.set("-Select-")

optionGender = OptionMenu(root, varGender, "-Select-", "Male", "Female")
optionGender.grid(row=70, column=10)

country = Label(root, text='Select your Country below')
country.grid(row=80, column=10)

varCountry = StringVar(root)
varCountry.set("-Select-")

cou = ["-Select-", "India", "USA", "Australia", "Canada"]

optionCountry = OptionMenu(root, varCountry, *cou)
optionCountry.grid(row=90, column=10)

email = Label(root, text='Enter your email')
email.grid(row=100, column=10)

emailEN = Entry(root)
emailEN.grid(row=110, column=10)

btn = Button(root, text='Submit', command=onClick)
btn.grid(row=120, column=10)


root.mainloop()
