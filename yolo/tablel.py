from bs4 import BeautifulSoup
import requests


response = requests.get('https://cse.gndec.ac.in/sites/default/files/TT%2017jul2018_data_and_timetable_years_days_horizontal.html#table_45')

soup = BeautifulSoup(response.text, "html.parser")
idTAG = soup.find_all('li')
tableNAME = []
year = []
for a in soup.find_all('a', href=True):
    if a.text:
        tableNAME.append(a['href'])
for x in idTAG:
    text = x.text
    year.append(text.strip())
for x in range(0,len(year)):
    print(x,'.',idTAG[x].text.strip())

for x in range(0, len(year)):
    i = int(input('Enter Year: '))
    z = tableNAME[i][1:]
    table = soup.find('table', {"id": "{}".format(z)})
    rows = table.find_all('tr')

    for  x in rows:
        print(x.text)





