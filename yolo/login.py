from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options, executable_path=r'/home/pulkit/Videos/chromedriver')
data = []
data_tr = []
def site_login():
    URL = 'https://academics.gndec.ac.in/'
    driver.get(URL)
    driver.find_element_by_id('username').send_keys('1615368')
    driver.find_element_by_id ('password').send_keys('anon@1234')
    python_button = driver.find_elements_by_xpath("/html/body/div/div[2]/div/div/form/button")[0]
    python_button.click()
    python_button1 = driver.find_elements_by_xpath("/html/body/div/div[2]/div/div/div[2]/form/button")[0]
    python_button1.click()
    a = driver.find_elements_by_tag_name('tr')
    for x in a:
        data_tr.append(x.text)
    driver.quit()


site_login()
print(data)
for x in data_tr:
    print(x)