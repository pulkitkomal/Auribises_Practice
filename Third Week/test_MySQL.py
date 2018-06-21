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
title.pack()

name = Label(root, text='Enter your name')
name.pack()

nameEN = Entry(root)
nameEN.pack()

age = Label(root, text='Enter your age')
age.pack()

ageEN = Entry(root)
ageEN.pack()

email = Label(root, text='Enter your email')
email.pack()

emailEN = Entry(root)
emailEN.pack()

address = Label(root, text='Enter your address')
address.pack()

addressEN = Entry(root)
addressEN.pack()

btn = Button(root, text='Submit', command=onClick)
btn.pack()

root.mainloop()


