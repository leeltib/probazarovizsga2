# 2 Feladat: Film register applikáció funkcióinak automatizálása

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html")


# TC-001 Betöltés után megjelenik-e a 24 film?
def mov_list_cont():
    time.sleep(4)
    mov_list_num = len(driver.find_elements_by_class_name('container-movies'))
    return mov_list_num


mov_list_start = mov_list_cont()

try:
    assert mov_list_start == 24
    print("Megjelenik a 24 film.")
except:
    print("Nem jelenik meg a 24 film.")
finally:
    pass


# TC-002
# Register gomb megnyomása
driver.find_element_by_xpath('/html/body/div[2]/div[1]/button').click()
time.sleep(3)

# megjelenő mezők kitöltése
driver.find_element_by_id("nomeFilme").send_keys("Black widow")
driver.find_element_by_id("anoLancamentoFilme").send_keys("2021")
driver.find_element_by_id("anoCronologiaFilme").send_keys("2020")
driver.find_element_by_id("linkTrailerFilme").send_keys("https://www.youtube.com/watch?v=Fp9pNPdNwjI")
driver.find_element_by_id("linkImagemFilme").send_keys("https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg")
driver.find_element_by_id("linkImdbFilme").send_keys("https://www.imdb.com/title/tt3480822/")

driver.find_element_by_xpath('/html/body/div[2]/div[2]/fieldset/button[1]').click()


# ellenőrzés:
mov_list_add = mov_list_cont()

try:
    assert mov_list_add == 25
    print("A mentett film felkerült a listára.")
except:
    print("Nem jelenik meg a felvett film.")
finally:
    pass

time.sleep(2)
driver.close()



