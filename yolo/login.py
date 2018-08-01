from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'/home/pulkit/Videos/chromedriver')

data = []
data_tr = []

def site_login():
    user = input('Enter Roll No.: ')
    passwrd = input('Enter Password: ')
    URL = 'https://academics.gndec.ac.in/'

    driver.get(URL)
    driver.find_element_by_id('username').send_keys('{}'.format(user))
    driver.find_element_by_id ('password').send_keys('{}'.format(passwrd))

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



def attendenceDATA():
    print()
    for x in range(0, 8):
        print(data_tr[x])
    y = 9
    z = 10
    totallect = 11
    lectureatt = 12
    j = 13
    booll = True
    um = 0

    for v in range(0,15):
        print()
        if um == 1:
            booll = True
        perc = float(data[j])
        totLECT= float(data[totallect])
        attLECT = float(data[lectureatt])
        print(data[y],data[z],'\nTotal Lectures: ',totLECT,'\nLectures Attented: ',attLECT,'\nPercentage:', perc,'%')
        y += 6
        z += 6
        j += 6
        totallect += 6
        lectureatt += 6
        p = totLECT
        q = attLECT
        needLECT = 0
        if(perc <= 75.00):
            while(booll):
                p = p + 1
                q = q + 1
                perc3 = (q / p) * 100
                lecNeed = q - attLECT
                needLECT = lecNeed
                if perc3 >= 75.00:
                    booll = False
                    um = 1


        else:
            pass
        if needLECT == 0:
            print('You can bunk this class!!')
        else:
            print('Lectures you need to attend for 75%: ',needLECT)

try:
    site_login()
    attendenceDATA()

except:
    pass
# 1615325
# qwerty12