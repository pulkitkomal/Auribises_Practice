import os
z = ['AFG', 'AUS', 'BAN', 'BER', 'CAN', 'EAF',
     'ENG', 'HOK', 'IND', 'IRE', 'KEN', 'NAM', 'NEP', 'NED', 'NZL', 'OMA',
     'PAK', 'PNG', 'SCO', 'SAF', 'SRL', 'UAE', 'USA', 'WIN', 'ZIM']

for country in z:
    try:
        os.remove("{}.csv".format(country))
    except:
        pass
    
    
