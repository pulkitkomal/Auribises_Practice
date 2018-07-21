from bs4 import BeautifulSoup
import requests
from urlextract import URLExtract
import urllib.request
import os


search = input()

searchAMAZON = search.replace(" ", "+")
URL = 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={}'.format(searchAMAZON)
response = requests.get(URL)
print(URL)
soup = BeautifulSoup(response.text,"lxml")
searchAMAZONresults = []
inrAMAZONresults = []
hrefAMAZONresults = []
images = []
def amazonDATA():
    searchAMAZONtags = soup.findAll('h2', class_="a-size-medium s-inline s-access-title a-text-normal")

    inrAMAZONtags = soup.findAll('span', class_="a-size-base a-color-price s-price a-text-bold")

    hrefAMAZONtags = soup.findAll('a', class_="a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal")

    image = soup.findAll('img')

    for text in searchAMAZONtags:
        searchAMAZONresults.append(text.text)

    for text2 in inrAMAZONtags:
        inrAMAZONresults.append(text2.text)

    extractor = URLExtract()

    for t in image:
        TEXT = str(t)
        URLS =  t.get('src')
        images.append(URLS)

    for tag in hrefAMAZONtags:
        text = str(tag)
        urls = extractor.find_urls(text)
        hrefAMAZONresults.append(urls)

    count = 0
    for x in range(3, len(images)):
        try:
            os.mkdir('amazonCache')
        except:
            pass
        amazonImage = images[x]
        fullfilename = os.path.join('amazonCache', '{}'.format(count))
        urllib.request.urlretrieve(amazonImage, fullfilename)
        count += 1


amazonDATA()

