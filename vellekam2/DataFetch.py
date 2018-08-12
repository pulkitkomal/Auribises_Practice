from bs4 import BeautifulSoup
import requests
import csv
import time
import os
import threading


class data1(threading.Thread):
    def run(self):
        starttime = time.time()
        z = ['AFG', 'AUS', 'BAN']

        for country in z:
            url = 'http://www.howstat.com/cricket/Statistics/Players/PlayerCountryList.asp?Country={}'.format(country)

            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')

            table = []

            for tr in soup.findAll('table', class_='TableLined'):
                for x in tr.findAll('td'):
                    z = x.text.strip()
                    if z == '':
                        table.append('0')
                    else:
                        table.append(z)

            init = 20
            last = 36
            # print('{}'.format(country))
            try:
                os.remove("{}.csv".format(country))
            except:
                pass
            head = ['Name', 'TESTSM', 'TESTSRuns', 'TESTSBat Avg', 'TESTSWkts', 'TESTSBowl Avg',
                    'ODIM', 'ODIRuns', 'ODIBat Avg', 'ODIWkts', 'ODIBowl Avg',
                    'T20M', 'T20Runs', 'T20Bat Avg', 'T20Wkts', 'T20Bowl Avg']
            with open("{}.csv".format(country), "a") as fp:
                wr = csv.writer(fp, dialect='excel')
                wr.writerow(head)

            for x in range(0, len(table) // 16 - 1):
                n = table[init:last]
                te = []
                # if n[0][-1:] == '*':
                #     print(n)
                # else:
                #     pass

                with open("{}.csv".format(country), "a") as fp:
                    wr = csv.writer(fp, dialect='excel')
                    wr.writerow(n)
                init += 16
                last += 16

        endtime = int(time.time() - starttime)
        print('Thread 1', endtime, 'seconds  ')


class data1_5(threading.Thread):
    def run(self):
        starttime = time.time()
        z = ['BER', 'CAN', 'EAF']

        for country in z:
            url = 'http://www.howstat.com/cricket/Statistics/Players/PlayerCountryList.asp?Country={}'.format(country)

            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')

            table = []

            for tr in soup.findAll('table', class_='TableLined'):
                for x in tr.findAll('td'):
                    z = x.text.strip()
                    if z == '':
                        table.append('0')
                    else:
                        table.append(z)

            init = 20
            last = 36
            # print('{}'.format(country))
            try:
                os.remove("{}.csv".format(country))
            except:
                pass
            head = ['Name', 'TESTSM', 'TESTSRuns', 'TESTSBat Avg', 'TESTSWkts', 'TESTSBowl Avg',
                    'ODIM', 'ODIRuns', 'ODIBat Avg', 'ODIWkts', 'ODIBowl Avg',
                    'T20M', 'T20Runs', 'T20Bat Avg', 'T20Wkts', 'T20Bowl Avg']
            with open("{}.csv".format(country), "a") as fp:
                wr = csv.writer(fp, dialect='excel')
                wr.writerow(head)

            for x in range(0, len(table) // 16 - 1):
                n = table[init:last]
                te = []
                # if n[0][-1:] == '*':
                #     print(n)
                # else:
                #     pass

                with open("{}.csv".format(country), "a") as fp:
                    wr = csv.writer(fp, dialect='excel')
                    wr.writerow(n)
                init += 16
                last += 16

        endtime = int(time.time() - starttime)
        print('Thread 1.5', endtime, 'seconds  ')


print()


class data2(threading.Thread):
    def run(self):
        starttime = time.time()
        z = ['ENG', 'HOK', 'IND']

        for country in z:
            url = 'http://www.howstat.com/cricket/Statistics/Players/PlayerCountryList.asp?Country={}'.format(country)

            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')

            table = []

            for tr in soup.findAll('table', class_='TableLined'):
                for x in tr.findAll('td'):
                    z = x.text.strip()
                    if z == '':
                        table.append('0')
                    else:
                        table.append(z)

            init = 20
            last = 36
            # print('{}'.format(country))
            try:
                os.remove("{}.csv".format(country))
            except:
                pass
            head = ['Name', 'TESTSM', 'TESTSRuns', 'TESTSBat Avg', 'TESTSWkts', 'TESTSBowl Avg',
                    'ODIM', 'ODIRuns', 'ODIBat Avg', 'ODIWkts', 'ODIBowl Avg',
                    'T20M', 'T20Runs', 'T20Bat Avg', 'T20Wkts', 'T20Bowl Avg']
            with open("{}.csv".format(country), "a") as fp:
                wr = csv.writer(fp, dialect='excel')
                wr.writerow(head)

            for x in range(0, len(table) // 16 - 1):
                n = table[init:last]
                te = []
                # if n[0][-1:] == '*':
                #     print(n)
                # else:
                #     pass

                with open("{}.csv".format(country), "a") as fp:
                    wr = csv.writer(fp, dialect='excel')
                    wr.writerow(n)
                init += 16
                last += 16

        endtime = int(time.time() - starttime)
        print('Thread 2', endtime, 'seconds  ')


class data2_5(threading.Thread):
    def run(self):
        starttime = time.time()
        z = ['IRE', 'KEN', 'NAM']

        for country in z:
            url = 'http://www.howstat.com/cricket/Statistics/Players/PlayerCountryList.asp?Country={}'.format(country)

            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')

            table = []

            for tr in soup.findAll('table', class_='TableLined'):
                for x in tr.findAll('td'):
                    z = x.text.strip()
                    if z == '':
                        table.append('0')
                    else:
                        table.append(z)

            init = 20
            last = 36
            # print('{}'.format(country))
            try:
                os.remove("{}.csv".format(country))
            except:
                pass
            head = ['Name', 'TESTSM', 'TESTSRuns', 'TESTSBat Avg', 'TESTSWkts', 'TESTSBowl Avg',
                    'ODIM', 'ODIRuns', 'ODIBat Avg', 'ODIWkts', 'ODIBowl Avg',
                    'T20M', 'T20Runs', 'T20Bat Avg', 'T20Wkts', 'T20Bowl Avg']
            with open("{}.csv".format(country), "a") as fp:
                wr = csv.writer(fp, dialect='excel')
                wr.writerow(head)

            for x in range(0, len(table) // 16 - 1):
                n = table[init:last]
                te = []
                # if n[0][-1:] == '*':
                #     print(n)
                # else:
                #     pass

                with open("{}.csv".format(country), "a") as fp:
                    wr = csv.writer(fp, dialect='excel')
                    wr.writerow(n)
                init += 16
                last += 16

        endtime = int(time.time() - starttime)
        print('Thread 2.5', endtime, 'seconds  ')


class data3(threading.Thread):
    def run(self):
        starttime = time.time()
        z = ['NEP', 'NED', 'NZL']

        for country in z:
            url = 'http://www.howstat.com/cricket/Statistics/Players/PlayerCountryList.asp?Country={}'.format(country)

            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')

            table = []

            for tr in soup.findAll('table', class_='TableLined'):
                for x in tr.findAll('td'):
                    z = x.text.strip()
                    if z == '':
                        table.append('0')
                    else:
                        table.append(z)

            init = 20
            last = 36
            # print('{}'.format(country))
            try:
                os.remove("{}.csv".format(country))
            except:
                pass
            head = ['Name', 'TESTSM', 'TESTSRuns', 'TESTSBat Avg', 'TESTSWkts', 'TESTSBowl Avg',
                    'ODIM', 'ODIRuns', 'ODIBat Avg', 'ODIWkts', 'ODIBowl Avg',
                    'T20M', 'T20Runs', 'T20Bat Avg', 'T20Wkts', 'T20Bowl Avg']
            with open("{}.csv".format(country), "a") as fp:
                wr = csv.writer(fp, dialect='excel')
                wr.writerow(head)

            for x in range(0, len(table) // 16 - 1):
                n = table[init:last]
                te = []
                # if n[0][-1:] == '*':
                #     print(n)
                # else:
                #     pass

                with open("{}.csv".format(country), "a") as fp:
                    wr = csv.writer(fp, dialect='excel')
                    wr.writerow(n)
                init += 16
                last += 16

        endtime = int(time.time() - starttime)
        print('Thread 3', endtime, 'seconds  ')


class data3_5(threading.Thread):
    def run(self):
        starttime = time.time()
        z = ['OMA', 'PAK', 'PNG']

        for country in z:
            url = 'http://www.howstat.com/cricket/Statistics/Players/PlayerCountryList.asp?Country={}'.format(country)

            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')

            table = []

            for tr in soup.findAll('table', class_='TableLined'):
                for x in tr.findAll('td'):
                    z = x.text.strip()
                    if z == '':
                        table.append('0')
                    else:
                        table.append(z)

            init = 20
            last = 36
            # print('{}'.format(country))
            try:
                os.remove("{}.csv".format(country))
            except:
                pass
            head = ['Name', 'TESTSM', 'TESTSRuns', 'TESTSBat Avg', 'TESTSWkts', 'TESTSBowl Avg',
                    'ODIM', 'ODIRuns', 'ODIBat Avg', 'ODIWkts', 'ODIBowl Avg',
                    'T20M', 'T20Runs', 'T20Bat Avg', 'T20Wkts', 'T20Bowl Avg']
            with open("{}.csv".format(country), "a") as fp:
                wr = csv.writer(fp, dialect='excel')
                wr.writerow(head)

            for x in range(0, len(table) // 16 - 1):
                n = table[init:last]
                te = []
                # if n[0][-1:] == '*':
                #     print(n)
                # else:
                #     pass

                with open("{}.csv".format(country), "a") as fp:
                    wr = csv.writer(fp, dialect='excel')
                    wr.writerow(n)
                init += 16
                last += 16

        endtime = int(time.time() - starttime)
        print('Thread 3', endtime, 'seconds  ')


class data4(threading.Thread):
    def run(self):
        starttime = time.time()
        z = ['SCO', 'SAF', 'SRL']

        for country in z:
            url = 'http://www.howstat.com/cricket/Statistics/Players/PlayerCountryList.asp?Country={}'.format(country)

            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')

            table = []

            for tr in soup.findAll('table', class_='TableLined'):
                for x in tr.findAll('td'):
                    z = x.text.strip()
                    if z == '':
                        table.append('0')
                    else:
                        table.append(z)

            init = 20
            last = 36
            # print('{}'.format(country))
            try:
                os.remove("{}.csv".format(country))
            except:
                pass
            head = ['Name', 'TESTSM', 'TESTSRuns', 'TESTSBat Avg', 'TESTSWkts', 'TESTSBowl Avg',
                    'ODIM', 'ODIRuns', 'ODIBat Avg', 'ODIWkts', 'ODIBowl Avg',
                    'T20M', 'T20Runs', 'T20Bat Avg', 'T20Wkts', 'T20Bowl Avg']
            with open("{}.csv".format(country), "a") as fp:
                wr = csv.writer(fp, dialect='excel')
                wr.writerow(head)

            for x in range(0, len(table) // 16 - 1):
                n = table[init:last]
                te = []
                # if n[0][-1:] == '*':
                #     print(n)
                # else:
                #     pass

                with open("{}.csv".format(country), "a") as fp:
                    wr = csv.writer(fp, dialect='excel')
                    wr.writerow(n)
                init += 16
                last += 16

        endtime = int(time.time() - starttime)
        print('Thread 4', endtime, 'seconds  ')


class data4_5(threading.Thread):
    def run(self):
        starttime = time.time()
        z = ['UAE', 'USA', 'WIN', 'ZIM']

        for country in z:
            url = 'http://www.howstat.com/cricket/Statistics/Players/PlayerCountryList.asp?Country={}'.format(country)

            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')

            table = []

            for tr in soup.findAll('table', class_='TableLined'):
                for x in tr.findAll('td'):
                    z = x.text.strip()
                    if z == '':
                        table.append('0')
                    else:
                        table.append(z)

            init = 20
            last = 36
            # print('{}'.format(country))
            try:
                os.remove("{}.csv".format(country))
            except:
                pass
            head = ['Name', 'TESTSM', 'TESTSRuns', 'TESTSBat Avg', 'TESTSWkts', 'TESTSBowl Avg',
                    'ODIM', 'ODIRuns', 'ODIBat Avg', 'ODIWkts', 'ODIBowl Avg',
                    'T20M', 'T20Runs', 'T20Bat Avg', 'T20Wkts', 'T20Bowl Avg']
            with open("{}.csv".format(country), "a") as fp:
                wr = csv.writer(fp, dialect='excel')
                wr.writerow(head)

            for x in range(0, len(table) // 16 - 1):
                n = table[init:last]
                te = []
                # if n[0][-1:] == '*':
                #     print(n)
                # else:
                #     pass

                with open("{}.csv".format(country), "a") as fp:
                    wr = csv.writer(fp, dialect='excel')
                    wr.writerow(n)
                init += 16
                last += 16

        endtime = int(time.time() - starttime)
        print('Thread 4.5', endtime, 'seconds  ')


def abc():
    print('Data update started!')

    ref = data1()
    ref1_5 = data1_5()

    ref2 = data2()
    ref2_5 = data2_5()

    ref3 = data3()
    ref3_5 = data3_5()

    ref4 = data4()
    ref4_5 = data4_5()

    ref.start()
    ref1_5.start()

    ref2.start()
    ref2_5.start()

    ref3.start()
    ref3_5.start()

    ref4.start()
    ref4_5.start()


abc()