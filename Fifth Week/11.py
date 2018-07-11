import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

response = requests.get("https://www.zomato.com/ludhiana/restaurants/")
print(response)
soup = BeautifulSoup(response.text,"html.parser")
print("=============================")
print("Restaurant Name",soup.title.text)
print(soup.prettify())