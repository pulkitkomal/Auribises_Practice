from bs4 import BeautifulSoup
import requests
from urlextract import URLExtract
# from home/pulkit/PycharmProjects/python_prac/Project import search_Input

search = input("a: ")

searchAMAZON = search.replace(" ", "+")
URL = 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={}'.format(searchAMAZON)
response = requests.get(URL)
print(URL)
soup = BeautifulSoup(response.text,"html.parser")
searchAMAZONresults = []
inrAMAZONresults = []
hrefAMAZONresults = []

def amazonDATA():
    searchAMAZONtags = soup.findAll('h2', class_="a-size-medium s-inline s-access-title a-text-normal")

    inrAMAZONtags = soup.findAll('span', class_="a-size-base a-color-price s-price a-text-bold")

    hrefAMAZONtags = soup.findAll('a', class_="a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal")

    for text in searchAMAZONtags:
        searchAMAZONresults.append(text.text)

    for text2 in inrAMAZONtags:
        inrAMAZONresults.append(text2.text)


    extractor = URLExtract()
    for tag in hrefAMAZONtags:
        text = str(tag)
        urls = extractor.find_urls(text)
        hrefAMAZONresults.append(urls)

amazonDATA()
print(searchAMAZONresults)
