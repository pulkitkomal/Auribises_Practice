from bs4 import BeautifulSoup
import requests
from urlextract import URLExtract


search = input('Enter the name of the product: ')

searchAMAZON = search.replace(" ", "+")
URL = 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={}'.format(searchAMAZON)
response = requests.get(URL)
print(URL)
soup = BeautifulSoup(response.text,"html.parser")
searchAMAZONresults = []
inrAMAZONresults = []
hrefAMAZONresults = []


# print(soup.prettify())
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

    count = 1
    x = 0
    y = 5
    for result in range(x,y):
        print(count,'. ', searchAMAZONresults[result], "--" ,end=" ")
        print('INR',inrAMAZONresults[result])
        count +=1
    dataIN = input('Would you like to view the rest?(Press 1 for yes or 2 for no) ')
    try:
        if dataIN == '1':
            for result in range(x+5, (len(inrAMAZONresults)-1)):
                print(count, '. ', searchAMAZONresults[result], "--", end=" ")
                print('INR', inrAMAZONresults[result])
                count += 1
        elif dataIN == '2':
            pass
        else:
            print('No valid input given!!')
            pass
    except:
        for result in range(x + 5, y+5):
            print(count, '. ', searchAMAZONresults[result], "--", end=" ")
            print('INR', inrAMAZONresults[result])
            count += 1
def amazonDETAILS():
    try:
        INPUT = int(input('Would you like to view details(Enter Number or press return to exit): '))
        descINPUT = INPUT - 1
        if INPUT == descINPUT + 1:
            desc = hrefAMAZONresults[descINPUT][0]
            print(desc)

            DESCresponse = requests.get('{}'.format(desc))

            soup = BeautifulSoup(DESCresponse.text, "html.parser")

            descTAG = soup.findAll('ul', class_='a-unordered-list a-vertical a-spacing-none')

            for t in descTAG:
                print(t.text)
    except:
        pass
def amazonGOBACK():
    loop = True
    while loop:
        retrn = input('Press return to exit or 1 to go back!')

        if retrn == '1':
            amazonDATA()
            amazonDETAILS()
        else:
            loop = False

amazonDATA()
amazonDETAILS()
amazonGOBACK()

