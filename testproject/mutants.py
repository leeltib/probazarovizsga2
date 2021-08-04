# 1 Feladat: Hogwards express jegyautomata

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html")

# elvárt eredmények listái (vizuális alapon -> a feladat kiírás szerint amit látunk, az helyes):
original_list_exp = ['angel', 'beast', 'cyclops', 'iceman', 'jean-grey', 'professor-x']
force_list_exp = ['angel', 'cyclops', 'nightcrawler', 'psylocke', 'rictor', 'storm', 'sunspot', 'wolverine']
factor_list_exp = ['angel', 'beast', 'cyclops', 'iceman', 'jean-grey', 'quicksilver', 'rictor']
hellfire_list_exp = ['angel', 'emma-frost', 'magneto', 'psylocke', 'storm', 'sunspot', 'tithe']

# csapattagok szűrése
teams = driver.find_elements_by_tag_name('li')

# kiolvasott adatokból létrehozott listák:
original_list = []
force_list = []
factor_list = []
hellfire_list = []

for char in teams:
    char_act = char.get_attribute('id')
    char_attr = char.get_attribute('data-teams').split()
    if 'original' in char_attr:
        original_list.append(char_act)
    if 'force' in char_attr:
        force_list.append(char_act)
    if 'factor' in char_attr:
        factor_list.append(char_act)
    if 'hellfire' in char_attr:
        hellfire_list.append(char_act)
    else:
        pass

# print(original_list)
# print(force_list)
# print(factor_list)
# print(hellfire_list)

# összehasonlítás:

def test_teams(team_exp, team, name):
    try:
        assert team_exp == team
        print(f'{name} csapat tagjai: OK')
    except:
        print(f'{name} csapat tagjai: FAIL')
    finally:
        pass


test_teams(original_list_exp, original_list, "Original X-Men")
test_teams(force_list_exp, force_list, "X-Force")
test_teams(factor_list_exp, factor_list, "X-Factor")
test_teams(hellfire_list_exp, hellfire_list, "Hellfire Club")

time.sleep(2)
driver.close()



