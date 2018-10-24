import pandas as pd


def data():

    z = ['AFG', 'AUS', 'BAN', 'BER', 'CAN', 'EAF', 'ENG', 'HOK', 'IND', 'IRE', 'KEN', 'NAM', 'NEP', 'NZL', 'OMA', 'PAK','PNG', 'SAF', 'SCO', 'SRL', 'UAE', 'USA', 'WIN', 'ZIM']

    for f in z:
        df = pd.read_csv('{}.csv'.format(f),sep=",",usecols=(0 , 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)) # To read 1st,2nd and 4th columns
        tstpt = 0.2*(df['TESTSM']) + 0.4*(df['TESTSRuns'] * 1.0 / 8.0) + (df['TESTSWkts']*4.0 - df['TESTSBowl Avg']*2.0)*0.4+100

        for x in range(0,len(tstpt)):
            if tstpt[x] == 100:
                tstpt[x] = 0.0
            else:
                pass


        df['Testpoints'] = tstpt
        odipt = 0.2*(df['ODIM']) + 0.4*(df['ODIRuns'] * 1.0 / 8.0) + (df['ODIWkts']*4.0 - df['ODIBowl Avg']*2.0)*0.4+100

        for x in range(0,len(odipt)):
            if odipt[x] == 100:
                odipt[x] = 0.0
            else:
                pass

        df['Odipoints'] = odipt
        t20pt = 0.2*(df['T20M']) + 0.4*(df['T20Runs'] * 1.0 / 8.0) + (df['T20Wkts']*4.0 - df['T20Bowl Avg']*2.0)*0.4+100

        for x in range(0,len(t20pt)):
            if t20pt[x] == 100:
                t20pt[x] = 0.0
            else:
                pass

        df['T20points'] = t20pt

        df.to_csv('{}.csv'.format(f),index=False)

