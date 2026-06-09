# Exemplo de uso de return
# Crie um programa em Python que tenha a função soma(x,y) que recebe dois números e retorna o valor da soma deles.
def soma(x,y):
    return (x+y)

a = int(input("Primeiro numero: "))
b = int(input("Segundo numero : "))
print("Soma: ", soma(a,b))



# ---------------------------------------------

# Exemplo de uso de return com Strings
# Crie um programa em Python que peça o nome e o sobrenome de uma pessoa, depois exiba na tela a mensagem "Olá sobrenome, nome".

def inverte(nome, sobrenome):
    nomeInverso = sobrenome+","+nome
    return nomeInverso

nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
invertido = inverte(nome,sobrenome)

print("Olá", invertido)

# -----------------------------------------

# Exemplos de return com Booleanos
# Crie um programa em Python que diz se o número inserido pelo usuário é par ou ímpar. Ele deve fazer isso através de uma função que recebe o inteiro e retorna True ou False.


# def eh_par(numero):
#     return numero % 2 == 0

# numero = int(input("Digite um número: "))
# if eh_par(numero):
#     print("O número é par.")
# else:
#     print("O número é ímpar.")

####################------------------------------------------------

def par(x):
    if (x%2)==0:
        return True
    else:
        return False

while True:
    num = int(input("Insira um número: "))
    if par(num):
        print("É par")
    else:
        print("É ímpar")


# -------------------------------------------------------------------

def cadastro():
    name = input("Qual seu nome: ")
    age   = int(input("Idade: ") )

    return name, age

print("Iniciando cadastro...")
nome, idade = cadastro()

print("Cadastro realizado com sucesso:")
print("Seu nome é", nome, "e você tem", idade,"anos de idade.")
