import mysql.connector
from tkinter import *


def onClick():
    name1 = nameEN.get()
    age1 = ageEN.get()
    email1 = emailEN.get()
    address1 = addressEN.get()
    con = mysql.connector.connect(user="root", password="", host="localhost", database="test")
    print("Is Connection Established:", con.is_connected())

    cursor = con.cursor()

    sql2 = "INSERT INTO `test` VALUES ('{}', '{}', '{}', '{}');".format(name1, age1, email1, address1)
    cursor.execute(sql2)
    con.commit()
    print("Saved !!")


root = Tk()


title = Label(root, text='Hello, please enter the details below! ')
title.grid(row=10,column=10)

name = Label(root, text='Enter your name')
name.grid(row=20,column=10)

nameEN = Entry(root)
nameEN.grid(row=30,column=10)

age = Label(root, text='Enter your age')
age.grid(row=40,column=10)

ageEN = Entry(root)
ageEN.grid(row=50,column=10)

email = Label(root, text='Enter your email')
email.grid(row=60,column=10)

emailEN = Entry(root)
emailEN.grid(row=70,column=10)

address = Label(root, text='Enter your address')
address.grid(row=80,column=10)

addressEN = Entry(root)
addressEN.grid(row=90,column=10)

btn = Button(root, text='Submit', command=onClick)
btn.grid(row=100,column=10)
root.resizable(False,False)
root.mainloop()


