from bs4 import BeautifulSoup
import requests
from urlextract import URLExtract
import urllib.request
import os
import shutil

user_INP = input('Input: ')
URL = "https://in.images.search.yahoo.com/search/images;_ylt=AwrxhddAyThceEkAsSS8HAx.;_ylc=X1MDMjExNDcyMzAwNARfcgMyBGJjawNkYjVrdGtwZHU3aTZmJTI2YiUzRDMlMjZzJTNEczUEZnIDBGdwcmlkA1FTVVZhdFhDU0FhS2IxT0hOSndKX0EEbXRlc3RpZANudWxsBG5fc3VnZwMxMARvcmlnaW4DaW4uaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzEEcHFzdHIDcmFjYwRwcXN0cmwDNARxc3RybAM3BHF1ZXJ5A3JhY2Nvb24EdF9zdG1wAzE1NDcyMjU0MjUEdnRlc3RpZANudWxs?gprid=QSUVatXCSAaKb1OHNJwJ_A&pvid=XOOHHjEwLjLVlp2mW.PIzwCwMjQwNQAAAAB84lH2&fr2=sa-gp-in.images.search.yahoo.com&p={}&ei=UTF-8&iscqry=&fr=sfp".format(user_INP)
response = requests.get(URL)

url_LIST = []
soup = BeautifulSoup(response.text,"html.parser")
extractor = URLExtract()

images = soup.find_all('img', class_='process')
for x in images:
    text = str(x)
    urls = extractor.find_urls(text)
    url_LIST.append(urls)
count = 0
print('Downloading started!')
try:
    shutil.rmtree('D:/ImageCACHE/{}'.format(user_INP))
except:
    pass
os.makedirs('D:/ImageCACHE/{}'.format(user_INP))
for x in url_LIST:
    urllib.request.urlretrieve(x[0], 'D:/ImageCACHE/{}/{}.jpg'.format(user_INP,count))
    count = count + 1
print('Downloading Complete!')