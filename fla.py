from Project import amazon
from Project import flipkart
from difflib import SequenceMatcher
import re
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    for x in amazon.searchAMAZONresults:
        for y in flipkart.nameRESULT:
            ratio = SequenceMatcher(None, x, y).ratio()
            # print(ratio)
            if ratio >= 0.90:
                v = amazon.inrAMAZONresults[amazon.searchAMAZONresults.index(x)].strip()
                d = re.sub('[\,]', '', v)
                s = flipkart.priceRESULT[flipkart.nameRESULT.index(y)]
                f = re.sub('[\,]', '', s)

                priceDIFF = int(d) - int(f)
                # print(' Difference in Price = ',priceDIFF )
                priceDIFFstr = str(priceDIFF)
                if priceDIFFstr[0] == '-':
                    return ('\n Price on Amazon for {} is {}\n'
                            '\n Price on Flipkart for {} is {}\n'
                            '\n The price is {}  cheaper on Amazon! \n'.format(x,d,y,f,priceDIFFstr[1:]))
                elif priceDIFFstr == '0':
                    return ('\n Price on Amazon for {} is {}\n'
                            '\n Price on Flipkart for {} is {}\n'
                            '\n The price is same on both websites! \n'.format(x,d,y,f,priceDIFFstr[1:]))
                else:
                    return ('\n Price on Amazon for {} is {}\n'
                            '\n Price on Flipkart for {} is {}\n'
                            '\n The price is {}  cheaper on Flipkart! \n'.format(x,d,y,f,priceDIFFstr))


if __name__ == '__main__':
    app.run()
