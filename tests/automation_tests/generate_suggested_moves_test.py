from selenium import webdriver
import time
from termcolor import colored

driver = webdriver.Chrome('./drivers/chromedriver.exe')

driver.get('http://127.0.0.1:5000/')
driver.set_page_load_timeout("30")

generate_moves_btn = driver.find_element_by_id('js-get-moves')
generate_moves_btn.click()
time.sleep(15)

alphabeta_prunning = driver.find_element_by_id('js-move-alphabeta_prunning')
hermann = driver.find_element_by_id('js-move-hermann')
ids_field = driver.find_element_by_id('js-move-ids')
minmax = driver.find_element_by_id('js-move-minmax')
negamax = driver.find_element_by_id('js-move-negamax')
#random
ruffian = driver.find_element_by_id('js-move-ruffian')
rybka = driver.find_element_by_id('js-move-rybka')
sos = driver.find_element_by_id('js-move-sos')
spike = driver.find_element_by_id('js-move-spike')
stockfish = driver.find_element_by_id('js-move-stockfish')


print(colored('generate_suggested_moves_button automation tests start...', 'green'))


try:
    assert alphabeta_prunning.text == 'e2e4'
    print(colored('Alphabeta_prunning field has been generated correctly', 'green'))
except AssertionError:
    print(colored('Alphabeta_prunning field was wrongly generated', 'red'))
try:
    assert hermann.text == 'e2e4'
    print(colored('Herman field has been generated correctly', 'green'))
except AssertionError:
    print(colored('Herman field was wrongly generated', 'red'))
try:
    assert ids_field.text == 'd2d4'
    print(colored('Ids field has been generated correctly', 'green'))
except AssertionError:
    print(colored('Ids field was wrongly generated', 'red'))
try:
    assert minmax.text == 'e2e4'
    print(colored('Minmax field has been generated correctly', 'green'))
except AssertionError:
    print(colored('Minmax field was wrongly generated', 'red'))
try:
    assert negamax.text == 'e2e4'
    print(colored('Negamax field has been generated correctly', 'green'))
except AssertionError:
    print(colored('Negamax field was wrongly generated', 'red'))
try:
    assert ruffian.text == 'e2e4'
    print(colored('Ruffian field has been generated correctly', 'green'))
except AssertionError:
    print(colored('Ruffian field was wrongly generated', 'red'))
try:
    assert rybka.text == 'b1c3'
    print(colored('Rybka field has been generated correctly', 'green'))
except AssertionError:
    print(colored('Rybka field was wrongly generated', 'red'))
try:
    assert sos.text == 'e2e4'
    print(colored('SOS field has been generated correctly', 'green'))
except AssertionError:
    print(colored('SOS field was wrongly generated', 'red'))
try:
    assert spike.text == 'e2e4'
    print(colored('Spike field has been generated correctly', 'green'))
except AssertionError:
    print(colored('Spike field was wrongly generated', 'red'))
try:
    assert stockfish.text == 'e2e4'
    print(colored('Stockfish field has been generated correctly', 'green'))
except AssertionError:
    print(colored('Stockfish field was wrongly generated', 'red'))
finally:
    driver.quit()
