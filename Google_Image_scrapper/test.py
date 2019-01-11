from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import urllib.request
driver = webdriver.Firefox(executable_path="D:/geckodriver.exe")

def img_search():
    # user_INP = input('Enter Roll No.: ')
    URL = "https://www.bing.com/images/search?q=raccoon&qs=AS&form=QBILPG&sp=1&pq=racc&sc=8-4&sk=&cvid=DF0ADDFCED2D40EBB8C362CAF1DDD0FC"

    driver.get(URL)
    # driver.find_element_by_id('username').send_keys()

    # inp = driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/form/div[2]/div/div[1]/div/div[1]/input")
    # inp.send_keys('{}'.format(user_INP))
    # submit = driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/form/div[2]/div/div[1]/button")
    imageXpathSelector = '/html/body/div[3]/div[5]/div[2]/div[1]/ul[1]/li[1]/div/div/a/div/img'
    img = driver.find_element_by_xpath(imageXpathSelector)
    src = (img.get_attribute('src'))
    urllib.request.urlretrieve(src, "a.jpg")
    driver.close()


img_search()