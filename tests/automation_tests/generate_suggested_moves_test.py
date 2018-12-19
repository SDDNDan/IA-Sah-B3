from selenium import webdriver
import time
from termcolor import colored

driver = webdriver.Chrome('./drivers/chromedriver.exe')

driver.get('http://127.0.0.1:5000/')
driver.set_page_load_timeout("30")

generate_moves_btn = driver.find_element_by_id('js-get-moves')
generate_moves_btn.click()
time.sleep(10)

ids_field = driver.find_element_by_id('js-move-ids')
alphabeta_prunning = driver.find_element_by_id('js-move-alphabeta_prunning')
negamax = driver.find_element_by_id('js-move-negamax')
stockfish = driver.find_element_by_id('js-move-stockfish')
minmax = driver.find_element_by_id('js-move-minmax')

print(colored('generate_suggested_moves_button automation tests start...', 'green'))

try:
    assert ids_field.text == 'd2d4'
    print(colored('Ids field has been generated correctly', 'green'))
except AssertionError:
    print(colored('Ids field was wrongly generated', 'red'))
try:
    assert alphabeta_prunning.text == 'd7d5'
    print(colored('Alphabeta_prunning field has been generated correctly', 'green'))
except AssertionError:
    print(colored('Alphabeta_prunning field was wrongly generated', 'red'))
try:
    assert negamax.text == 'g7g5'
    print(colored('Negamax field has been generated correctly', 'green'))
except AssertionError:
    print(colored('Negamax field was wrongly generated', 'red'))
try:
    assert stockfish.text == 'f8e7'
    print(colored('Stockfish field has been generated correctly', 'green'))
except AssertionError:
    print(colored('Stockfish field was wrongly generated', 'red'))
try:
    assert minmax.text == 'e2e4'
    print(colored('Minmax field has been generated correctly', 'green'))
except AssertionError:
    print(colored('Minmax field was wrongly generated', 'red'))
finally:
    driver.quit()
