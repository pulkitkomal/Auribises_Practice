from Project import amazon
from Project import flipkart
from difflib import SequenceMatcher
import re

for x in amazon.searchAMAZONresults:
    for y in flipkart.nameRESULT:
        ratio = SequenceMatcher(None, x, y).ratio()
        # print(ratio)
        if ratio >= 0.90:
            v = amazon.inrAMAZONresults[amazon.searchAMAZONresults.index(x)].strip()
            d = re.sub('[\,]', '', v)
            s = flipkart.priceRESULT[flipkart.nameRESULT.index(y)]
            f = re.sub('[\,]', '', s)
            print(x,d)
            print(y,f)
            priceDIFF = int(d) - int(f)
            # print(' Difference in Price = ',priceDIFF )
            priceDIFFstr = str(priceDIFF)
            if priceDIFFstr[0] == '-':
                print('\nThe price is {}  cheaper on Amazon! \n'.format(priceDIFFstr[1:]))
            elif priceDIFFstr == '0':
                print('\nThe price is same on both websites! \n'.format(priceDIFFstr[1:]))
            else:
                print('\nThe price is {}  cheaper on Flipkart! \n'.format(priceDIFFstr))

        elif ratio >= 0.70:
            v = amazon.inrAMAZONresults[amazon.searchAMAZONresults.index(x)].strip()
            d = re.sub('[\$,]', '', v)
            s = flipkart.priceRESULT[flipkart.nameRESULT.index(y)]
            f = re.sub('[\$,]', '', s)
            print(x,d)
            print(y,f)
            priceDIFF = int(d) - int(f)
            # print(' Difference in Price = ',priceDIFF )
            priceDIFFstr = str(priceDIFF)
            if priceDIFFstr[0] == '-':
                print('\nThe price is {}  cheaper on Amazon! \n'.format(priceDIFFstr[1:]))
            elif priceDIFFstr == '0':
                print('\nThe price is same on both websites! \n'.format(priceDIFFstr[1:]))
            else:
                print('\nThe price is {}  cheaper on Flipkart! \n'.format(priceDIFFstr))

        elif ratio >= 0.50:
            v = amazon.inrAMAZONresults[amazon.searchAMAZONresults.index(x)].strip()
            d = re.sub('[\$,]', '', v)
            s = flipkart.priceRESULT[flipkart.nameRESULT.index(y)]
            f = re.sub('[\$,]', '', s)
            print(x,d)
            print(y,f)
            priceDIFF = int(d) - int(f)
            # print(' Difference in Price = ',priceDIFF )
            priceDIFFstr = str(priceDIFF)
            if priceDIFFstr[0] == '-':
                print('\nThe price is {}  cheaper on Amazon! \n'.format(priceDIFFstr[1:]))
            elif priceDIFFstr == '0':
                print('\nThe price is same on both websites! \n'.format(priceDIFFstr[1:]))
            else:
                print('\nThe price is {}  cheaper on Flipkart! \n'.format(priceDIFFstr))