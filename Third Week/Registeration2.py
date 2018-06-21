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

    output = "{} belongs to {}, {} age is {} & {} email id is {}".format(Name, Country, gender, Age, gender, Email)
    print(output)


root = Tk()

title = Label(root, text='Enter your details below!!')
title.grid(row=0, column=0)

name = Label(root, text='Enter your name')
name.grid(row=20)

nameEN = Entry(root)
nameEN.grid(row=20, column=10)

age = Label(root, text='Enter your age')
age.grid(row=30,)

ageEN = Entry(root)
ageEN.grid(row=30, column=10)

Gender = Label(root, text='Select your Gender')
Gender.grid(row=40)

varGender = StringVar(root)
varGender.set("-Select-")

optionGender = OptionMenu(root, varGender, "-Select-", "Male", "Female")
optionGender.grid(row=40, column=10)

country = Label(root, text='Select your Country')
country.grid(row=50)

varCountry = StringVar(root)
varCountry.set("-Select-")

cou = ["-Select-", "India", "USA", "Australia", "Canada"]

optionCountry = OptionMenu(root, varCountry, *cou)
optionCountry.grid(row=50, column=10)

email = Label(root, text='Enter your email')
email.grid(row=60)

emailEN = Entry(root)
emailEN.grid(row=60, column=10)

btn = Button(root, text='Submit', command=onClick)
btn.grid(row=70, column=5)


root.mainloop()
