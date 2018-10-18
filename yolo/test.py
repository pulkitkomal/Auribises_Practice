from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options, executable_path="/home/pulkit/Videos/geckodriver")

data = []
data_tr = []

URL = 'https://www.amazon.in/s?url=search-alias%3Daps&field-keywords=iphone+6s'
driver.get(URL)

print(driver.find_elements_by_tag_name('span'))