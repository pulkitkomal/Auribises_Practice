import requests
from bs4 import BeautifulSoup
countryNAME = input()
response = requests.get("http://www.howstat.com/cricket/Statistics/Players/PlayerCountryList.asp?Country={}".format(countryNAME))

soup = BeautifulSoup(response.text,"html.parser")


tags = soup.find_all('td')
for x in tags:
    print(x.text.strip())