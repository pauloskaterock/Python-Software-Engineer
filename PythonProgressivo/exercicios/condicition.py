# Faça um programa que pergunta o gênero da pessoa. Se ela for mulher, digite 1. Se for homem, digite 2. Outro, 3.

# Para cada um, ele deve exibir uma mensagem dizendo o gênero escolhido.


# print('Ola buenas')

# genero = input('Qual o seu genero?')

# if genero == '1':
#     print('Você é do gênero feminino.')
# elif genero == '2':
#     print('Você é do gênero masculino.')
# elif genero == '3':
#     print('Você é de outro gênero.')
# else:
#     print('Opção inválida.')

#--------------------------------------------------------------
# import pyautogui
# import pyautogui as escolha_opcao

# # abre a message box com opçoes
# opcao = pyautogui.confirm('Clica no botao desejada meu consagrado' , buttons = ['1', '2', '3'])


sexo = int( input('Digite 1 se for mulher, 2 homem ou 3 outro: ') )

if sexo == 1:
    print('Você é mulher')
if sexo == 2:
    print('Vocè é homem')
if sexo == 3:
    print('Outro gênero')
