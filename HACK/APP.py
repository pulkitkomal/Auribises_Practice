from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt


class facebookDATA:

    def plotGraph(self): #data sourced from Recode
        data = pd.read_csv("RecodeDATA.csv")
        X = data["Year"].values
        Y = data["Ages0"].values
        Z = data["Ages12"].values
        A = data["Ages18"].values
        ax = plt.subplot(111)
        ax.bar(X - 0.2, Y, width=0.2, color='b', align='center', label='Ages 0-12')
        ax.bar(X, Z, width=0.2, color='g', align='center', label='Ages 12-17')
        ax.bar(X + 0.2, A, width=0.2, color='r', align='center', label='Ages 18-24')
        plt.legend()
        plt.title('Percentage in decrease in Usage')
        plt.show()

    def plotIFS(self): #data sourced from Google Trends
        data = pd.read_csv("DATAIFS.csv")
        X = data["Year"].values
        Y = data["Facebook"].values
        Z = data["Instagram"].values
        A = data["Snapchat"].values
        ax = plt.subplot(111)
        ax.bar(X - 0.2, Y, width=0.2, color='b', align='center', label='Facebook')
        ax.bar(X, Z, width=0.2, color='g', align='center', label='Instagram')
        ax.bar(X + 0.2, A, width=0.2, color='r', align='center', label='Snapchat')
        plt.legend()
        plt.title('Annual change in monthly usage (In Percentage)')
        plt.show()

    def plotG(self): #data sourced from Google Trends
        data = pd.read_csv("FBSign.csv")
        X = data["Week"].values
        Y = data["facebook signup: (Worldwide)"].values
        plt.figure(figsize=(20, 5))
        plt.bar(X , Y, width=0.2, color='b', align='center')
        plt.title('Google Search Analytics')
        plt.show()


ref = facebookDATA()

root = Tk()
root.title('Facebook Data')

space1 = Label(root, text='Number of Active Users Decrease   ').grid(row=20, column=0)
btn2 = Button(root, text='Plot Graph', command=ref.plotGraph).grid(row=20, column=5)

space2 = Label(root, text='Sign Up Google Search Data   ').grid(row=30, column=0)
btn3 = Button(root, text='Plot Graph', command=ref.plotG).grid(row=30, column=5)

space3 = Label(root, text='Annual change in monthly usage   ').grid(row=40, column=0)
btn4 = Button(root, text='Plot Graph', command=ref.plotIFS).grid(row=40, column=5)

space4 = Label(root, text='       ')
space4.grid(row=50, column=0)

root.resizable(False, False)
root.mainloop()

#Team Sourav & Pulkit