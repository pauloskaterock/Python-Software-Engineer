import pyautogui as posicaoAbreArquivos


print('-------------------------Abrindo Notepad------------------------')
posicaoAbreArquivos.hotkey('win', 'r')

posicaoAbreArquivos.sleep(4)
posicaoAbreArquivos.typewrite('notepad')
posicaoAbreArquivos.press('enter')
posicaoAbreArquivos.sleep(2)
# posicaoAbreArquivos.click('OK')
posicaoAbreArquivos.typewrite('notepad aberto com Python robo')
posicaoAbreArquivos.sleep(2)


fecharJanela = posicaoAbreArquivos.getActiveWindow()
posicaoAbreArquivos.sleep(2)
fecharJanela.close()

posicaoAbreArquivos.sleep(2)
posicaoAbreArquivos.press('tab')
posicaoAbreArquivos.sleep(2)
posicaoAbreArquivos.press('enter')

print('-------------------------Fechando e Finalizando Notepad...')
