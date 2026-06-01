# def teste():
#   print("estamos dentro da função")
#   var = 2112
#   print("valor de var:", var)

# teste()
# print("agora estamos fora da função")
# print("valor de var:", var)

# ---------------------------------------------------

def teste():
    banda="Rush"
    print("A melhor banda do mundo é ", banda)
    teste2()

def teste2():
    banda="Beatles"
    print("A melhor banda do mundo é ", banda)
    teste3()

def teste3():
    banda="Iron Maiden"
    print("A melhor banda do mundo é ", banda)

teste()

# print(teste2)


# -------------------------------------------------


# Exemplo de Função com Parâmetro e Argumento

# Crie um programa que peça ao usuário dois valores. Estes números deverão ser repassados para uma função chamada calculadora, que vai mostrar a soma, subtração, divisão e multiplicação desses números.

def calculadora(x,y):
    print("Soma          =",x+y)
    print("Subtração     =",x-y)
    print("Divisão       =",x/y)
    print("Multiplicação =",x*y)

primeiro = float(input("Primeiro número: "))
segundo  = float(input("Segundo número: "))

calculadora(primeiro,segundo)


# -----------------------------------------------------

# Crie um script em Python que pede uma frase (string) ao usuário e em seguida um caractere. Em seguida, seu script deve dizer quantas vezes aquele caracte.re apareceu na frase digitar. Use função com parâmetros

def conta_caractere(texto,char):
    count = 0
    for letra in texto:
        if letra == char:
            count += 1
    print(char,"apareceu",count,"vezes na string")

string=input("Digite um texto qualquer: ")
caractere = input("Digite um caractere: ")

conta_caractere(string,caractere)

# --------------------------------------------------------

# Exercícios Propostos

# 01. Crie uma função que recebe um número e exiba seu quadrado.
# 02. Crie uma função que recebe um valor e exiba seu cubo.
# 03. Crie uma função que recebe 4 notas de um aluno, e exiba a média dele.
# 04. Crie uma função que recebe 3 números e exiba o maior deles.
