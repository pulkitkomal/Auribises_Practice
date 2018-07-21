from bs4 import BeautifulSoup
import requests
from Project import search_Input


inp = search_Input.search_INPUT

URLinput = inp.replace(" ", "+")
URL = 'https://www.flipkart.com/search?q={}'.format(URLinput)
print(URL)
response =  requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

nameRESULT = []
priceRESULT = []
links_with_text = []
linkURL = []
# print(soup.prettify())
def try1():
    nameTAGrequest = soup.findAll('div', class_='_3wU53n')
    priceTAGrequest = soup.findAll('div', class_='_1vC4OE _2rQ-NK')


    for tag in nameTAGrequest:
        nameRESULT.append(tag.text)

    for tag in priceTAGrequest:
        priceRESULT.append(tag.text[1:])

    for a in soup.find_all('a', class_='_31qSD5', href=True):
        if a.text:
            links_with_text.append(a['href'])

    count = 1
    a = 8
    for x in range (0,10):
        link = 'https://flipkart.com'+links_with_text[x]
        linkURL.append(link)
        a += 1
        count +=1

def try2():
    for a in soup.find_all('a', class_='_2cLu-l', title=True):
        if a.text:
            nameRESULT.append(a['title'])

    priceTAGrequest = soup.findAll('div', class_='_1vC4OE')

    for tag in priceTAGrequest:
        priceRESULT.append(tag.text[1:])

    for a in soup.find_all('a', class_='_1Vfi6u', href=True):
        if a.text:
            links_with_text.append(a['href'])
    count = 1
    for x in range(0, len(nameRESULT)):
        link = 'https://flipkart.com' + links_with_text[x]
        linkURL.append(link)
        count += 1

try:
    try1()
except:
    try2()
