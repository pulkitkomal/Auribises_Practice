from flask import Flask, request, render_template, redirect, url_for
from bs4 import BeautifulSoup
import requests
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from tkinter import *
import time


app = Flask(__name__,template_folder='/home/pulkit/PycharmProjects/python_prac/FL/template')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
movie = []
a_time = []
year = []

@app.route('/')
def index():
    return render_template('index.html')

def plotGraph():
    data = pd.read_csv("/home/pulkit/PycharmProjects/python_prac/FL/static/tempDATA.csv")
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
    plt.title('Next movie estimated time is {}'.format(pv))
    plt.xlabel('Year')
    plt.ylabel('Time')
    plt.grid(True)
    plt.plot(X, Y, "o")
    plt.plot(X, Y1)
    plt.savefig('/home/pulkit/PycharmProjects/python_prac/FL/static/plot1.png')

@app.route('/', methods=['GET','POST'])
def my_form_post():

    genre = request.form['genre']
    sdate = request.form['sdate']
    edate = request.form['edate']
    totmovies = request.form['totmovies']
    print('Data Scrapping Started !!!')
    link = 'https://www.imdb.com/search/title?genres={}&countries=in&sort=year,asc&count={}&title_type=feature&release_date={},{}-12-31&runtime=1,1000'.format(
        genre, totmovies, sdate, edate)
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")

    tagMOVIE = soup.find_all('span', class_='userRatingValue')
    tagMOVIE_list = []
    for x in tagMOVIE:
        z = str(x)
        text = z[43:52]
        tagMOVIE_list.append(text)

    nameMOVIE = soup.find_all('img', class_='loadlate')
    for x in nameMOVIE:
        e = str(x)
        z = e.replace(',', '.')
        y = z.find('class')
        nameOfMovie = z[10: y - 2]
        movie.append(nameOfMovie)

    timeTAG = soup.find_all('span', class_='runtime')
    for x in timeTAG:
        t = str(x.text[:-4])
        z = int(t)
        a_time.append(z)

    yearTAG = soup.find_all('span', class_='lister-item-year text-muted unbold')
    for x in yearTAG:
        z = str(x.text)
        a = re.findall(r'\d+', z)
        year.append(a[0])

    print(movie)
    print(a_time)
    print(year)
    dataset = list(zip(movie, a_time, year))
    df = pd.DataFrame(data=dataset, columns=["Movie", "Time", "Year"])
    df.to_csv("/home/pulkit/PycharmProjects/python_prac/FL/static/tempDATA.csv", index=False, header=True)
    moviesNUM = 'Data taken from number of movies : {}'.format(len(movie))
    yearsNUM = '\nMovies from Year {} to {}'.format(year[0],year[len(year) - 1])
    plotGraph()
    time.sleep(3)
    return render_template('output.html', moviesNUM = moviesNUM, yearsNUM = yearsNUM)

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1,firefox=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


