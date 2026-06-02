# # 1Robô "Lançador de Apps"pyautogui, timeCriar um script que abre o Menu Iniciar (ou equivalente), digita o nome de um aplicativo (ex: Bloco de Notas, Calculadora) e pressiona Enter. Demonstra controle básico do teclado.




# import pyautogui
# import time
# import sys #  biblioteca para sair de erros caso a automação de erros


# # define um ponto de fahano canto superior esquerdo

# pyautogui.FAILSAVE = True
# # variaveis de configuração
# APP_NAME = "notepad"
# DELAY_START = 3 # tempo em segundos para o usuario posicionar o objeto
# DELAY_ACTION = 0.5


# def iniciar_aplicativo(app_nome: str):
#   """
#     Simula o usuário abrindo o Menu Iniciar, digitando o nome do app
#     e pressionando Enter.

#     Args:
#         app_nome (str): O nome do aplicativo a ser lançado (ex: 'notepad').
#     """
#     printf("---A automação em inicio esta---")
#     printf(f"O script ira começar em {DELAY_START} segundos is good be change the window voce deve")
#     time.sleep(DELAY_START)

# print(f"Pressionando tecla 'win' (Windows) ou 'command' (macOS)...")
# pyautogui.press('win')
# time.sleep(DELAY_ACTION) # espera o menu Abrir


# print(f"digitando o nome do aplicativo{app.capitalize()}")
# pyautogui.write(app_nome)
# time.sleep(DELAY_ACTION) # Espera a busca carregar

# print("pressionando enter para executar")
# pyautogui.press('enter')


# print("automação concluida esta pequeno gafanhoto")

# if __name__ == "__main__":
#     try:
#         # Pede confirmação ou simplesmente executa o robô
#         iniciar_aplicativo(APP_NAME)
#     except pyautogui.FailSafeException:
#         # A exceção é capturada se o mouse for movido para o canto (0, 0)
#         print("\n--- ERRO: Automação interrompida pelo FailSafe! ---")
#         sys.exit()
#     except Exception as e:
#         print(f"\n--- ERRO CRÍTICO: Ocorreu um erro inesperado: {e} ---")
#         sys.exit()
