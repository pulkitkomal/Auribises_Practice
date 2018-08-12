import requests
from bs4 import BeautifulSoup
import html5lib
import requests

import os
url= "http://howstat.com/cricket/Statistics/Players/PlayerCountryList.asp?Country=IND"
response = requests.get(url)
soup= BeautifulSoup(response.text,"html.parser")
playerdata=playerdatasaved=''
for tags in soup.findAll('table',class_='TableLined'):
    #print(tags.text)
    playerdata=''
    for x in tags.find_all('td'):
        playerdata = playerdata.strip()+","+x.text.strip()
        print(playerdata)
        #print(playerdata)
        #if len(playerdata) != 0:
        #    playerdatasaved = playerdatasaved + playerdata[1:]
#print(playerdata)
header = "Name,	TM,	TRuns,	TBatAvg,	TWkts,	TBowlAvg,	OM,	ORuns,	OBatAvg,OWkts,OBowlAvg,T2M,	T2Runs,T2BatAvg,T2Wkts,T2Bowl Avg"
file = open(os.path.expanduser("INDIA PLAYERS.csv"),"wb")
file.write(bytes(header,encoding="ascii",errors="ignore"))

file.write(bytes(playerdata,encoding="ascii",errors="ignore"))