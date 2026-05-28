# # "Crie um programa que imprima na tela os números 1 até o 10, usando o laço while"

# # ---------------------WHILE--------------------------
# numero=1

# while numero<=10:
#     print(numero)
#     numero += 1
# # --------------------------------------------------------

# # "Faça um programa que peça um número maior que 1 ao usuário. Em seguida, imprima todos os números, de 1 até o número que o usuário informou"


# numero=1
# max = int(input("Digite um inteiro maior que 1: ") )

# while numero <= max:
#     print(numero)
#     numero += 1


# # -------------------------------------------------

# # "Escreva um programa que repita pra sempre, na tela, a mensagem 'Curso Python Progressivo'".

# # while True:
# #     print("Curso Python Progressivo")



# # ----------------------------------------------------

# # "Crie um programa que peça um número ao usuário e imprima todos os números pares de 1 até o número fornecido"


# numero=1
# max = int(input("Digite um inteiro maior que 1: ") )

# print("Numeros pares entre 1 e", max, ":")

# while numero <= max:
#     if numero%2==0:
#         print(numero,  end=" ") # O end=" " é para mostrar um espaço em branco após imprimir cada número, ao invés de quebra de linha (enter).
#     numero+=1


# # -----------------------------------------------------

# # "Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem corretamente a senha"


# senha='2112'
# tentativa=input("Digite a senha:")

# # != diferente de
# while (senha != tentativa):
#     print("Senha errada! Tente novamente!")
#     tentativa=input("Digite a senha:")

# print("Senha correta. Entrando no sistema...")


# # ------------------------------------------------------------

# # "Programe um script em Python que calcule a média de uma turma, não importa o número de alunos que ela tenha, seu único script serve para todos os casos"


# alunos=int(input("Numeros de alunos na turma: "))

# count=1
# soma = 0.0
# while count <= alunos:
#     print("Nota do aluno ", count, ":")
#     nota = float( input() )
#     soma += nota
#     count += 1

# print("Media da turma: ", (soma/alunos) )


# # ---------------------------------------------------------

# # ----------------------FOR ---------------------------------------------


# # Crie um script em Python que imprima os números de 1 até 5 na tela."

# # Nossa sequência é: 1, 2, 3, 4, 5
# # Então, nosso código fica:

# for val in [1,2,3,4,5]:
#     print('os valores sao:',val)



# # ------------------------------------------------------------------

# # "Crie um script que imprime todos os dias da semana na tela."

# # Não é obrigatório usarmos números na sequência. Uma lista pode ser formada de strings, por exemplo.

# # Nosso código fica:

# for dia in ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']:
#     print(dia)



# # ----------------------- RANGE ---------------------------------

# # "Crie um script em Python que imprima os números de 1 até 5 na tela, usando a função range."

# # Nosso código fica assim:

# for val in range(5):
#     print(val+1)




# # Crie um script em Python que imprima os números de 1 até 5 na tela, usando a função range como elemento de início e o de fim

# for val in range(1, 6):
#     print(val)




# # Crie um script em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada


# tabuada = int(input("Qual tabuada fazer: ") )

# for var in range(1,11):
#     print(tabuada*var)



# # Crie um programa que pergunte ao usuário o termo inicial e a razão de uma PA.
# # Em seguida, pergunte a ele quantos elementos da PA ele deseja que seja impresso, e imprima todos os elementos dessa progressão Aritmética, do primeiro termo até o termo 'n' escolhido pelo usuário.


# primeiro=int(input("Primeiro elemento: ") )
# razao = int(input("Razao: ") )
# n = int(input("Quantos elementos exibir: ") )

# ultimo = primeiro + (n-1)*razao
# ultimo = ultimo + 1

# for var in range(primeiro, ultimo, razao):
#     print(var)



# # ---------------------EXPRESSOES---OPERACOES---ATRIBUICAO--------------------------

# # Crie um programa que peça um número inteiro positivo ao usuário.
# # Em seguida, o script deve mostrar os números de 0 até o valor que o usuário escolheu. Use WHILE


# n=int(input("Digite um inteiro positivo: ") )

# count=0
# while count <= n:
#     print(count)
#     count = count + 1





# # Crie um programa em Python que pede um número inteiro ao usuário e calcule seu fatorial.

# numero = int(input("Fatorial de: ") )

# resultado=1
# for n in range(1,numero+1):
#     resultado *= n

# print(resultado)



# # Exercício de Python
# # Seu  professor de Matemática, cansado de ficar fazendo multiplicações para achar o fatorial, te encomendou um script em Python (obviamente pagou, pois você possui um certificado do curso de Python).

# # Porém, ele quer fazer vários e vários cálculos.
# # Nos exemplos anteriores a gente pede o número uma vez, mostra o fatorial e fecha o script.

# # Ele não, ele quer um looping infinito, que só acabe quando ele fornecer o número 0 como entrada.


# while True:
#     numero = int(input("Fatorial de (0 para sair): "))
#     if numero == 0:
#         break
#     resultado = 1
#     for n in range(1, numero + 1):
#         resultado *= n
#     print(resultado)



# # ---------------------LO0PS ANINHADOS---------------------------------------

# # Faça um programa em Python que solicite um número positivo inteiro ao usuário, e depois exiba um tabuleiro na tela, com igual número de linhas e colunas


# print("Vamos criar um tabuleiro de tamanho:  N x N")
# n=int(input("Valor de N: ") )

# for linha in range(n):
#     for coluna in range(n):
#         print("x  ",end='')
#     print()









# # Crie um programa que exiba todos os segundos e minutos no intervalo de uma hora, no seguinte formato: XXmin YYs
# # Por exemplo:
# # 12min59s

# for minutos in range(60):
#     for segundos in range(60):
#         print(minutos,"min",segundos,"s")




# # Faça um script em Python que exiba todos os possíveis palpites da Mega-Sena.
# # Dados:
# # Cada palpite possui 6 dezenas
# # As dezenas variam de 1 até 60
# # Não pode repetir dezena


# total=0
# for dez1 in range(60):
#     for dez2 in range(dez1+1,60):
#         for dez3 in range(dez2+1,60):
#             for dez4 in range(dez3+1,60):
#                 for dez5 in range(dez4+1,60):
#                     for dez6 in range(dez5+1,60):
#                         total += 1
# print(total)


# # -------------------------------ELSE--BREAK-CONTINUE-----------------------------------

# # Escreva um programa em Python que vai somar todos os números de 1 até 1 milhão, menos os que são múltiplos de 3


# total=0

# for count in range(1000000):
#     count += 1
#     if(count % 3 == 0 ): continue
#     total += count

# print(total)


#--------------------------------------EXERCICIOS--------------------------------------

# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("Insira uma nota 0 até 10: "))

while (nota < 0) or (nota > 10):
    nota = float(input("Não pode ser menor que 0 ou maior que 10 meu jovem!\n \
    Tente novamente:"))
print("Nota válida")


# ---------------------------------------------------------------------------

# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

login = input("Login: ")
senha = input("Senha: ")

while login == senha:
    print("Sua senha deve ser diferente do login: ")
    senha = input("Senha: ")

print("Cadastro aprovado")

# ------------------------------------------------------------------------


# 03.Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';


nome = input("Qual seu nome [minimo 4 caracteres]: ")
idade = int(input("Sua idade: "))
salario = float(input("Salário: "))
sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ")
civil = input("Estado civil (s, c, v ou d): ")

while len(nome) <= 3:
    nome = input("Seu nome deve ter mais que 3 caracteres: ")

while (idade < 0) or (idade > 150):
    idade = int(input("Voce deve ter entre 0 e 150 anos: "))

while (salario<0):
    salario = float(input("A coisa ta difícil, mas não tem salário negativo: "))

while (sexo!= 'f') and (sexo!='m'):
    sexo = input("Biologicamente, você deve ser 'f' ou 'm': ")

while (civil!='s')and(civil!='c')and(civil!='v')and(civil!='d'):
    print("Nao tem estado civil 'confuso'")
    civil = input("Deve ser s, c, v ou d: ")


# --------------------------------------------------

# 04. e 05.
# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.


popA=int(input("População do país A: "))
while popA<0:
    popA=int(input("População do país deve ser maior que 0: "))
taxaA=float(input("Taxa de crescimento da cidade A: "))

popB=int(input("População do país B: "))
while popB<0:
    popB=int(input("População do país deve ser maior que 0: "))
taxaB=float(input("Taxa de crescimento da cidade B: "))

ano=0
while popA < popB:
    ano += 1
    popA = int((1 + (taxaA/100) )* popA)
    popB = int((1 + (taxaB/100) )* popB)
    print("Ano %d:" % ano)
    print("Populaçao A: %d" % popA)
    print("População B: %d\n\n" % popB)

print("Ultrapassa no ano:",ano)
