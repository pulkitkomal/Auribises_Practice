from bs4 import BeautifulSoup
import requests
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import threading
from tkinter import *
import os



class imdbMOVIES(threading.Thread):
    def url(self):
        genre = lbl_EN.get()
        sdate = lbl2_EN.get()
        edate = lbl3_EN.get()
        totmovies = lbl4_EN.get()
        print(type(genre))
        link = 'https://www.imdb.com/search/title?genres={}&countries=in&sort=year,asc&count={}&title_type=feature&release_date={},{}-12-31&runtime=1,1000'.format(genre,totmovies,sdate,edate)
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")

        tagMOVIE = soup.find_all('span', class_='userRatingValue')
        tagMOVIE_list = []
        for x in tagMOVIE:
            z = str(x)
            text = z[43:52]
            tagMOVIE_list.append(text)

        nameMOVIE = soup.find_all('img', class_='loadlate')
        movie = []
        for x in nameMOVIE:
            z = str(x)
            y = z.find('class')
            nameOfMovie = z[10: y - 2]
            movie.append(nameOfMovie)

        timeTAG = soup.find_all('span', class_='runtime')
        time = []
        for x in timeTAG:
            t = str(x.text[:-4])
            z = int(t)
            time.append(z)

        yearTAG = soup.find_all('span', class_='lister-item-year text-muted unbold')
        year = []
        for x in yearTAG:
            z = str(x.text)
            a = re.findall(r'\d+', z)
            year.append(a[0])

        print(movie)
        print(time)
        print(year)
        try :
            os.remove('tempDATA.csv')
        except:
            pass

        dataset = list(zip(movie, time, year))
        df = pd.DataFrame(data=dataset, columns=["Movie", "Time", "Year"])
        df.to_csv("tempDATA.csv", index=False, header=True)
        moviesSPACE.config(text = 'Data taken from number of movies : {}'.format(len(movie)))
        yearSPACE.config(text = 'Movies from Year {} to {}'.format(year[0],year[len(year) - 1]))

    def run(self):
        imdbMOVIES.url(self)
        space2.config(text = 'Data Scraped')


def plotGraph():
    data = pd.read_csv("tempDATA.csv")
    X = data["Year"].values
    Y = data["Time"].values

    data = stats.linregress(X,Y)
    b1 = data[0]
    b0 = data[1]

    Y1 = []

    for x in X:
        y = b0 + (b1*x)
        Y1.append(y)
    pv = Y1[len(Y1) - 1]
    plt.title('Next movie predicted time is {}'.format(pv))
    plt.xlabel('Year')
    plt.ylabel('Time')
    plt.grid(True)
    plt.plot(X, Y, "o")
    plt.plot(X, Y1)
    plt.show()

ref = imdbMOVIES()

def st():
    ref.start()

root = Tk()

root.title('Movie Duration Prediction')
lbl = Label(root, text='Enter Genre').grid(row=0, column=0)
lbl_EN = Entry(root)
lbl_EN.grid(row=0, column=10)

genre = Label(root , text = 'Genre : Action, Biography, Comedy\n'
                            'Crime, Family, Music\n'
                            'Romance, Thriller').grid(row = 10, column = 0)
space1 = Label(root, text='           \n            ').grid(row=20, column=0)

lbl2 = Label(root, text='Enter Starting Year').grid(row=20, column=0)
lbl2_EN = Entry(root)
lbl2_EN.grid(row=20, column=10)
space3 = Label(root, text='           ').grid(row=30, column=0)

lbl3 = Label(root, text='Enter Ending Year').grid(row=40, column=0)
lbl3_EN = Entry(root)
lbl3_EN.grid(row=40, column=10)
space4 = Label(root, text='           ').grid(row=50, column=0)

lbl4 = Label(root, text='Enter Maximum Number of Movies').grid(row=60, column=0)
lbl4_EN = Entry(root)
lbl4_EN.grid(row=60, column=10)
space5 = Label(root, text='           ').grid(row=70, column=0)

btn = Button(root, text='Submit', command= st).grid(row=80, column=0)
btn2 = Button(root, text='Show Answer', command= plotGraph).grid(row=80, column=5)

space2 = Label(root, text='       ')
space2.grid(row=90, column=0)

moviesSPACE = Label(root, text='       ')
moviesSPACE.grid(row=100, column=0)

yearSPACE = Label(root, text='       ')
yearSPACE.grid(row=110, column=0)

root.resizable(False, False)
root.mainloop()
