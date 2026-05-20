import pyautogui
import pyautogui as escolha_opcao

# abre a message box com opçoes notepad,excel, word
opcao = pyautogui.confirm('Clica no botao desejada meu consagrado' , buttons = ['Notepad', 'Excel', 'Word'])


if opcao == 'Notepad':
    print("Notepad selecionado")
    escolha_opcao.sleep(2)

    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.typewrite('notepad')
    escolha_opcao.press('enter')

elif opcao == 'Excel':
    print("Excel selecionado")
    escolha_opcao.sleep(2)
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.typewrite('excel')
    escolha_opcao.press('enter')

elif opcao == 'Word':
    print("Word selecionado")
    escolha_opcao.sleep(2)
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.typewrite('word')
    escolha_opcao.press('enter')
