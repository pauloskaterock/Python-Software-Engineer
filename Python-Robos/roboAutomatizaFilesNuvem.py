# Robo que automatiza a cópia de um arquivo local para a nuvem


# import logging
import pyautogui
import time

import logging

# configuração Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
)


pyautogui.alert("O robo automatizador ira iniciar, não mexa em seua maquina")
pyautogui.PAUSE = 0.5

logging.info('Aplicação iniciada com sucesso.')


# abrir o google drive em sua Pasta
logging.info('Iniciando navegação no Google Drive.')
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
# pyautogui.press('enter')

logging.info('Pressionando Ctrl, l.')
pyautogui.hotkey('ctrl' , 'l')


logging.info('Escrevendo no google Drive.')
pyautogui.write('https://drive.google.com/drive/my-drive')
time.sleep(1)
pyautogui.press('enter')

# entrar na area de trabalho
pyautogui.hotkey('winleft', 'd')

# clica no arquivo e copia e arrasta ele
logging.info('clica no arquivo e copia e arrasta ele.')
pyautogui.moveTo(953,45)

pyautogui.mouseDown()

pyautogui.moveTo(953, 516)

pyautogui.hotkey('alt' , 'tab')
time.sleep(1)

pyautogui.alert("O robo automatizador acabou de finalizar, pode mexer em seua maquina novamente")

logging.info('Finalizando Automação.')

print("Robo finalizado")
