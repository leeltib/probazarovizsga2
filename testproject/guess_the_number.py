# 3 Feladat: Guess the number automatizálása

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html")

# felhasznált mezők definiálása, állapotuk kiolvasása
restart_button = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/button")
guess_input = driver.find_element_by_xpath("/html/body/div/div[2]/input")
guess_button = driver.find_element_by_xpath("/html/body/div/div[2]/span/button")

guess_lower = driver.find_element_by_xpath("/html/body/div/p[3]")
guess_higher = driver.find_element_by_xpath("/html/body/div/p[4]")
guess_yes = driver.find_element_by_xpath("/html/body/div/p[5]")

num_of_guesses = driver.find_element_by_xpath('/html/body/div/div[3]/p/span').text

# a szám keresése:
restart_button.click()

num_steps = 0
for i in range(100):
    guess_input.clear()
    guess_input.send_keys(i+1)
    guess_button.click()
    num_steps += 1
    time.sleep(0.5)
    guess_yes_contr = guess_yes.get_attribute('class')
    if guess_yes_contr == "alert alert-success":
        break

# a szükséges lépések számának ellenőrzése:
time.sleep(1)
num_of_guesses = driver.find_element_by_xpath('/html/body/div/div[3]/p/span').text
print(num_of_guesses)
print(num_steps)

try:
    assert int(num_of_guesses) == num_steps
    print("Az alkalmazás és az általam számolt lépésszám egyezik.")
except:
    print("Az alkalmazás és az általam számolt lépésszám NEM egyezik.")
finally:
    pass


# intervallumon kívüli számokkal való tesztelés:
def test_inv_num(num, sel, re):
    restart_button.click()
    guess_input.send_keys(num)
    guess_button.click()
    contr = sel.get_attribute('class')
    try:
        assert contr == "alert alert-warning"
        print(f'A {num}-re megfelelő, "{re}" válasszal reagált az alkalmazás.')
    except:
        print(f'A {num}-re nem megfelelő válasszal reagált az alkalmazás.')


test_inv_num('-19', guess_higher, "Guess higher")

test_inv_num('255', guess_lower, "Guess lower")

time.sleep(2)
driver.close()

