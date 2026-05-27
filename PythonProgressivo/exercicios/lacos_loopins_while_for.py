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




# Crie um script em Python que imprima os números de 1 até 5 na tela, usando a função range como elemento de início e o de fim

for val in range(1, 6):
    print(val)




# Crie um script em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada


tabuada = int(input("Qual tabuada fazer: ") )

for var in range(1,11):
    print(tabuada*var)



# Crie um programa que pergunte ao usuário o termo inicial e a razão de uma PA.
# Em seguida, pergunte a ele quantos elementos da PA ele deseja que seja impresso, e imprima todos os elementos dessa progressão Aritmética, do primeiro termo até o termo 'n' escolhido pelo usuário.


primeiro=int(input("Primeiro elemento: ") )
razao = int(input("Razao: ") )
n = int(input("Quantos elementos exibir: ") )

ultimo = primeiro + (n-1)*razao
ultimo = ultimo + 1

for var in range(primeiro, ultimo, razao):
    print(var)



# ---------------------EXPRESSOES---OPERACOES---ATRIBUICAO--------------------------

# Crie um programa que peça um número inteiro positivo ao usuário.
# Em seguida, o script deve mostrar os números de 0 até o valor que o usuário escolheu. Use WHILE


n=int(input("Digite um inteiro positivo: ") )

count=0
while count <= n:
    print(count)
    count = count + 1





# Crie um programa em Python que pede um número inteiro ao usuário e calcule seu fatorial.

numero = int(input("Fatorial de: ") )

resultado=1
for n in range(1,numero+1):
    resultado *= n

print(resultado)



# Exercício de Python
# Seu  professor de Matemática, cansado de ficar fazendo multiplicações para achar o fatorial, te encomendou um script em Python (obviamente pagou, pois você possui um certificado do curso de Python).

# Porém, ele quer fazer vários e vários cálculos.
# Nos exemplos anteriores a gente pede o número uma vez, mostra o fatorial e fecha o script.

# Ele não, ele quer um looping infinito, que só acabe quando ele fornecer o número 0 como entrada.


while True:
    numero = int(input("Fatorial de (0 para sair): "))
    if numero == 0:
        break
    resultado = 1
    for n in range(1, numero + 1):
        resultado *= n
    print(resultado)



# ---------------------LO0PS ANINHADOS---------------------------------------

# Faça um programa em Python que solicite um número positivo inteiro ao usuário, e depois exiba um tabuleiro na tela, com igual número de linhas e colunas


print("Vamos criar um tabuleiro de tamanho:  N x N")
n=int(input("Valor de N: ") )

for linha in range(n):
    for coluna in range(n):
        print("x  ",end='')
    print()









# Crie um programa que exiba todos os segundos e minutos no intervalo de uma hora, no seguinte formato: XXmin YYs
# Por exemplo:
# 12min59s

for minutos in range(60):
    for segundos in range(60):
        print(minutos,"min",segundos,"s")




# Faça um script em Python que exiba todos os possíveis palpites da Mega-Sena.
# Dados:
# Cada palpite possui 6 dezenas
# As dezenas variam de 1 até 60
# Não pode repetir dezena


total=0
for dez1 in range(60):
    for dez2 in range(dez1+1,60):
        for dez3 in range(dez2+1,60):
            for dez4 in range(dez3+1,60):
                for dez5 in range(dez4+1,60):
                    for dez6 in range(dez5+1,60):
                        total += 1
print(total)
