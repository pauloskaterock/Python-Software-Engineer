print('Funções em Python')

def hello_word():
	print('Essa Função imprime uma mensagem HELLO PYTHON')

# return hello_word
hello_word()

# -----------------------------------------------------------

# Exemplo de Código com Funções
# Crie uma função que pede dois números, faz a soma e exibe o resultado, através de uma função. O usuário pode executar a função quantas vezes desejar.

print('função em python')

def soma():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    soma = x + y
    print("Soma: ",soma)

continuar=1

while continuar:
    if(continuar):
        soma()
    continuar=int(input("Digite 0 se desejar encerrar ou qualquer outro numero para continuar: "))

#     else: continuar=! 0
# print('vamos continuar')


# ------------------------------------------------------

# Faça uma calculadora, usando funções. O script pergunta qual operação o usuário deseja rodar (soma, subtração, multiplicação ou divisão) e executa a operação.

# A calculadora deve ser executada quantas vezes o usuário desejar.

print('----------Calculadora Com Funções ----------')
def soma():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Soma: ",x+y)

def subtracao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Subtracao: ",x-y)

def multiplicacao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Multiplicacao: ",x*y)

def divisao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Divisao: ",x/y)

opcao=1

while opcao:
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")

    opcao = int(input("Opção: "))

    if(opcao==1):
        soma()
    if(opcao==2):
        subtracao()
    if(opcao==3):
        multiplicacao()
    if(opcao==4):
        divisao()
