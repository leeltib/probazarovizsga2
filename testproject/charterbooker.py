# 4 Feladat: charterbooker automatizálása

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html")


# első oldal kitöltése:
def page_1():
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="step1"]/ul/li[1]/select/option[3]').click()
    driver.find_element_by_xpath('//*[@id="step1"]/ul/li[2]/button').click()


page_1()


# mezők meghatározása, kitöltése a második oldalon:
def page_2():
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="step2"]/ul/li[1]/input').send_keys('2021-08-21')
    driver.find_element_by_xpath('//*[@id="step2"]/ul/li[2]/select/option[2]').click()
    driver.find_element_by_xpath('//*[@id="step2"]/ul/li[3]/select/option[2]').click()
    driver.find_element_by_xpath('//*[@id="step2"]/ul/li[4]/button').click()


page_2()


# mezők meghatározása, kitöltése a harmadik oldalon:
def page_3(mail):
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="step3"]/ul/li[1]/input').send_keys('Katalin Szabó')
    driver.find_element_by_xpath('//*[@id="step3"]/ul/li[2]/input').send_keys(mail)
    driver.find_element_by_xpath('//*[@id="step3"]/ul/li[3]/textarea').send_keys('I have no questions.')
    driver.find_element_by_xpath('//*[@id="step3"]/ul/li[4]/button').click()


page_3('katszab@gmail.com')


# elfogadó szöveg ellenőrzése:
time.sleep(2)
text_h2 = driver.find_element_by_xpath('//*[@id="booking-form"]/h2').text
print(text_h2)
text_exp = "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!)."
print(text_exp)

try:
    assert text_h2 == text_exp
    print("Az elfogadó szöveg OK.")
except:
    print("Az elfogadó szöveg NEM megfelelő!")


# email cím validációja:
time.sleep(1)
driver.refresh()
time.sleep(2)

page_1()
page_2()
page_3('katszab.gmail.com')

time.sleep(1)
error_text = driver.find_element_by_xpath('//*[@id="bf_email-error"]').text
print(error_text)

try:
    assert error_text == "PLEASE ENTER A VALID EMAIL ADDRESS."
    print("Email validáció OK!")
except:
    print("Hibás email cím elfogadva!")
finally:
    pass

time.sleep(2)
driver.close()

