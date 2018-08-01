from selenium import webdriver

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
    b = driver.find_elements_by_tag_name('td')
    for x in b:
        data.append(x.text)

    driver.quit()


site_login()
for x in range(0,8):
    print(data_tr[x])

def lecNeeded(p, q):
    print("lec needed called")
    p=p+1
    q=q+1
    print(p,q)
    perc2=(q/p)*100
    print(perc2)
    lecNeed = q - needLECT
    print(lecNeed)
    return lecNeed


y = 9
z = 10
totallect= 11
lectureatt = 12
j = 13

try:
    for v in range(0,15):
        print()
        perc = float(data[j])
        totLECT= float(data[totallect])
        needLECT = float(data[lectureatt])
        print(data[y],data[z],'\nTotal Lectures: ',totLECT,'\nLectures Attented: ',needLECT,'\nPercentage:', perc,'%')
        y += 6
        z += 6
        j += 6
        totallect += 6
        lectureatt += 6
        perc2=perc
        if(perc2<75.00):
            p = totLECT
            q = needLECT
            res = lecNeeded(p, q)

        print(res)


except:
    pass