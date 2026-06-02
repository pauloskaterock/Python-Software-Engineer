# importando  modulos
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import logging



# abrindo navegador
nav = webdriver.Chrome() # instanciando o navegador


# abrindo navegador
nav.get("https://www.google.com")


# digitar na busca
nav.find_element(By.NAME, 'q' ).send_keys('Thrasher Magazine')


# clica para buscar
nav.find_element(By.NAME, 'btnK').click()
time.sleep(10)


# pesquisar revista de skate

# nav.find_element(By.ID, 'More').text
nav.find_element(By.CLASS_NAME, 'More').text


nav.quit()
