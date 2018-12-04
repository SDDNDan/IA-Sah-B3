from selenium import webdriver

import time

# Selenium se instaleaza prin comanda "pip install -U selenium"
from selenium.webdriver.common.keys import Keys

# Fiecare browser are driverul lui dar pentru primul test voi folosi doar chrome
driver = webdriver.Chrome(
    "C:\\Users\\Dan\\Desktop\\IA-Sah-B3\\documentation\\qa\\automation-test\\drivers\\chromedriver.exe")

# Daca nu reusesc sa ma conectez la site in maxim 30 secunde programul va iesi automat
driver.set_page_load_timeout("30")

# Arrange

# Incerc sa ma conectez la github ( Pagina principala )
driver.get("https://github.com")

# Caut elementul de Sign In dupa xpath
driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]").send_keys(Keys.ENTER)
username = "Numele tau"
password = "Parola ta"
time.sleep(5)

# Caut elementul unde imi pun numele dupa "nume"
driver.find_element_by_name("login").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("commit").send_keys(Keys.ENTER)

# Aici mia fost greu sa il gasesc la search si am facut in felul urmator
# Am cautat div cu toate repositorurile
# Am cautat care din ele contine IA-SAH-B3
driver.find_element_by_css_selector(
    "div[class*=\"js-repos-container\"] a[data-hovercard-url*=\"IA-Sah-B3\"]").send_keys(Keys.ENTER)

try:
    driver.find_element_by_css_selector("button[title*=Star]").send_keys(Keys.ENTER)
    time.sleep(5)
except:
    pass

driver.quit()
