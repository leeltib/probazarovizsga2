# 5 Feladat: Periodusos rendszer

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html")


# elemek kigyűjtése egy listába:

time.sleep(2)
li_full = driver.find_elements_by_tag_name('li')

elements = []
for elem in li_full:
    elem_act = []
    elem_num = elem.get_attribute('data-pos')
    if elem_num != None:
        elem_name = elem.find_element_by_tag_name('span').text
        elem_act.append(elem_num)
        elem_act.append(elem_name)
        elements.append(elem_act)
    else:
        continue

print(elements)


# összehasonlítás az ellenőrző listával:

with open('data.txt', 'r', encoding='utf-8') as file:
    txt_elements = file.readlines()

list_txt = []
for txt_element in txt_elements:
    elem = txt_element.strip().replace(" ", "").split(',')
    list_txt.append(elem)

print(list_txt)

try:
    assert elements == list_txt
    print("Az elemek sorrendje megegyezik.")
except:
    print("Az elemek sorrendje NEM egyezik meg!")

time.sleep(2)
driver.close()
