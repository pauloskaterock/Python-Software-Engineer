# "Crie um programa que imprima na tela os números 1 até o 10, usando o laço while"

# ---------------------WHILE--------------------------
numero=1

while numero<=10:
    print(numero)
    numero += 1
# --------------------------------------------------------

# "Faça um programa que peça um número maior que 1 ao usuário. Em seguida, imprima todos os números, de 1 até o número que o usuário informou"


numero=1
max = int(input("Digite um inteiro maior que 1: ") )

while numero <= max:
    print(numero)
    numero += 1


# -------------------------------------------------

# "Escreva um programa que repita pra sempre, na tela, a mensagem 'Curso Python Progressivo'".

# while True:
#     print("Curso Python Progressivo")



# ----------------------------------------------------

# "Crie um programa que peça um número ao usuário e imprima todos os números pares de 1 até o número fornecido"


numero=1
max = int(input("Digite um inteiro maior que 1: ") )

print("Numeros pares entre 1 e", max, ":")

while numero <= max:
    if numero%2==0:
        print(numero,  end=" ") # O end=" " é para mostrar um espaço em branco após imprimir cada número, ao invés de quebra de linha (enter).
    numero+=1


# -----------------------------------------------------

# "Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem corretamente a senha"


senha='2112'
tentativa=input("Digite a senha:")

# != diferente de
while (senha != tentativa):
    print("Senha errada! Tente novamente!")
    tentativa=input("Digite a senha:")

print("Senha correta. Entrando no sistema...")


# ------------------------------------------------------------

# "Programe um script em Python que calcule a média de uma turma, não importa o número de alunos que ela tenha, seu único script serve para todos os casos"


alunos=int(input("Numeros de alunos na turma: "))

count=1
soma = 0.0
while count <= alunos:
    print("Nota do aluno ", count, ":")
    nota = float( input() )
    soma += nota
    count += 1

print("Media da turma: ", (soma/alunos) )


# ---------------------------------------------------------

# ----------------------FOR ---------------------------------------------


# Crie um script em Python que imprima os números de 1 até 5 na tela."

# Nossa sequência é: 1, 2, 3, 4, 5
# Então, nosso código fica:

for val in [1,2,3,4,5]:
    print('os valores sao:',val)



# ------------------------------------------------------------------

# "Crie um script que imprime todos os dias da semana na tela."

# Não é obrigatório usarmos números na sequência. Uma lista pode ser formada de strings, por exemplo.

# Nosso código fica:

for dia in ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']:
    print(dia)



# ----------------------- RANGE ---------------------------------

# "Crie um script em Python que imprima os números de 1 até 5 na tela, usando a função range."

# Nosso código fica assim:

for val in range(5):
    print(val+1)
