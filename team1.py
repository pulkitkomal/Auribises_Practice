import csv

name = []

testm = []
testruns = []
testbatavg = []
testswkts = []
testsbowlavg = []

ODIm = []
ODIruns = []
ODIbatavg = []
ODIwkts = []
ODIbowlavg = []

T20m = []
T20runs = []
T20batavg = []
T20wkts = []
T20bowlavg = []

def dataEXT():
    countryName = input('Enter Country Name: ')

    f = open("{}.csv".format(countryName))
    reader = csv.DictReader(f)

    for row in reader:
        Name = row["Name"]
        # if Name[-1:] == '*':
        name.append(Name)
        Testm = row["TESTSM"]
        testm.append(Testm)
        Testruns = row["TESTSRuns"]
        testruns.append(Testruns)
        Testbatavg = row["TESTSBat Avg"]
        testbatavg.append(Testbatavg)
        Testswkts = row["TESTSWkts"]
        testswkts.append(Testswkts)
        Testsbowlavg = row["TESTSBowl Avg"]
        testsbowlavg.append(Testsbowlavg)

        odim = row["ODIM"]
        ODIm.append(odim)
        odiruns = row["ODIRuns"]
        ODIruns.append(odiruns)
        odibatavg = row["ODIBat Avg"]
        ODIbatavg.append(odibatavg)
        odiwkts = row["ODIWkts"]
        ODIwkts.append(odiwkts)
        odibowlavg = row["ODIBowl Avg"]
        ODIbowlavg.append(odibowlavg)

        t20m = row["T20M"]
        T20m.append(t20m)
        t20runs = row["T20Runs"]
        T20runs.append(t20runs)
        t20batavg = row["T20Bat Avg"]
        T20batavg.append(t20batavg)
        t20wkts = row["T20Wkts"]
        T20wkts.append(t20wkts)
        t20bowlavg = row["T20Bowl Avg"]
        T20bowlavg.append(t20bowlavg)

team1PLAYER = []
team1TestPoints = []
team1ODIPoints = []
team1T20Points = []
# print(name)
# a = input('Input: ')
def TEAM1():
    for player in name:
        if player[-1:] == '*':
            x = name.index(player)
            pla = name[x]
            team1PLAYER.append(pla)
            # print(pla)

            TM = float(testm[x])
            TR = float(testruns[x])
            TBatA = float(testbatavg[x])
            TW = float(testswkts[x])
            TBowlA = float(testsbowlavg[x])
            tpoints = TM + (TR * 0.25) + (TW * 4) + (TBatA / 8)
            # print(tpoints)
            team1TestPoints.append(tpoints)

            OM = float(ODIm[x])
            OR = float(ODIruns[x])
            OBatA = float(ODIbatavg[x])
            OW = float(ODIwkts[x])
            OBowlA = float(ODIbowlavg[x])
            opoints = OM + (OR * 0.25) + (OW * 4) + (OBatA / 8)
            # print(opoints)
            team1ODIPoints.append(opoints)

            T20M = float(T20m[x])
            T20R = float(T20runs[x])
            T20BatA = float(T20batavg[x])
            T20W = float(T20wkts[x])
            T20BowlA = float(T20bowlavg[x])
            T20points = T20M + (T20R * 0.25) + (T20W * 4) + (T20BatA / 8)
            # print(T20points)
            team1T20Points.append(T20points)

    for player in name:
        if player[-1:] == '*':
            pass
        else:
            x = name.index(player)
            pla = name[x]
            team1PLAYER.append(pla)
            # print(pla)

            TM = float(testm[x])
            TR = float(testruns[x])
            TBatA = float(testbatavg[x])
            TW = float(testswkts[x])
            TBowlA = float(testsbowlavg[x])
            tpoints = TM + (TR * 0.25) + (TW * 4) + (TBatA / 8)
            # print(tpoints)
            team1TestPoints.append(tpoints)

            OM = float(ODIm[x])
            OR = float(ODIruns[x])
            OBatA = float(ODIbatavg[x])
            OW = float(ODIwkts[x])
            OBowlA = float(ODIbowlavg[x])
            opoints = OM + (OR * 0.25) + (OW * 4) + (OBatA / 8)
            # print(opoints)
            team1ODIPoints.append(opoints)

            T20M = float(T20m[x])
            T20R = float(T20runs[x])
            T20BatA = float(T20batavg[x])
            T20W = float(T20wkts[x])
            T20BowlA = float(T20bowlavg[x])
            T20points = T20M + (T20R * 0.25) + (T20W * 4) + (T20BatA / 8)
            # print(T20points)
            team1T20Points.append(T20points)

    # print(team1PLAYER)
    # print(team1TestPoints)
    # print(team1ODIPoints)
    # print(team1T20Points)

