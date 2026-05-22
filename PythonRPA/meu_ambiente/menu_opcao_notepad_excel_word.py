import pyautogui
import pyautogui as escolha_opcao


# import tkinter as tk
# from tkinter import messagebox

# # Janela personalizada com tkinter
# root = tk.Tk()
# root.withdraw()  # Esconde a janela principal

# # Customização da mensagem
# messagebox.showinfo(
#     "Título da Janela",  # title
#     "Clique no botão desejado meu consagrado"  # text

# )

# ------------------------------------
# abre a message box com opçoes notepad,excel, word
opcao = pyautogui.confirm('Clica no botao desejada meu consagrado' , buttons = ['Notepad', 'Excel', 'Word', 'vscode'])


if opcao == 'Notepad':
    print("Notepad selecionado")
    escolha_opcao.sleep(2)

    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.typewrite('notepad')
    escolha_opcao.press('enter')


    print(escolha_opcao.position(x=371, y=303))
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('notepad aberto com Python robo')

elif opcao == 'Excel':
    print("Excel selecionado")
    escolha_opcao.sleep(2)
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.typewrite('excel')
    escolha_opcao.press('enter')

    print(escolha_opcao.position(x=371, y=303))
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('Excel aberto com Python robo')

elif opcao == 'Word':
    print("Word selecionado")
    escolha_opcao.sleep(2)
    escolha_opcao.hotkey('win', 'r')
    escolha_opcao.typewrite('word')
    escolha_opcao.press('enter')

    print(escolha_opcao.position(x=371, y=303))
    escolha_opcao.sleep(2)
    escolha_opcao.typewrite('Word aberto com Python robo')

# elif opcao == 'vscode':
#     print("vscode selecionado")
#     escolha_opcao.sleep(2)
#     escolha_opcao.hotkey('win', 'r')
#     escolha_opcao.typewrite('vscode')
#     escolha_opcao.press('enter')
