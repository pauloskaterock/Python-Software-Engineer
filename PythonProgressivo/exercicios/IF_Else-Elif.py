# Escreva um código que exiba o nome de dois times, em seguida pergunta ao usuário qual deles é o melhor.

# Com a resposta em mãos, usando IF e ELSE, imprima na tela uma mensagem dizendo qual time ele torce.


# time1 = input("Digite o nome do primeiro time: ")
# time2 = input("Digite o nome do segundo time: ")

# resposta = input(f"Qual time você torce? {time1} ou {time2}? ")

# if resposta == time1:
#     print(f"Você torce para o {time1}!")
# else:
#     print(f"Você torce para o {time2}!")


# ---------------------------------------------------------

# Faça um programa que peça dois números e imprima o maior deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior número é: {num1}")
else:
    print(f"O maior número é: {num2}")

# ----------------------------------------------------------

# Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.

# valor = int(input("Digite um valor: "))

# if valor > 0:
#     print("O valor é positivo.")
# else:
#     print("O valor é negativo.")


num=int( input('Digite um numero: ') )

if num > 0 :
    print('Positivo')
else:
    if num == 0 :
        print('Nem positivo nem negativo, é 0')
    else:
        print('Negativo')


# -----------------------------------------------------


# Crie um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra_feminina = 'F'
letra_masculina = 'M'

letra = input("Digite uma letra (F/M): ")

if letra == letra_feminina:
    print("F - Feminino")
elif letra == letra_masculina:
    print("M - Masculino")
else:
    print("Sexo Inválido")

# ------------------------------------------------------

# Crie um programa em Python que peça a nota do aluno, que deve ser um float entre 0.00 e 10.0

# Se a nota for menor que 6.0, deve exibir a nota F.
# Se a nota for de 6.0 até 7.0, deve exibir a nota D.
# Se a nota for entre 7.0 e 8.0, deve exibir a nota C.
# Se a nota for entre 8.0 e 9.0, deve exibir a nota B.

# Por fim, se for entre 9.0 e 10.0, deve exibir um belo de um A.

nota = float(input('Digite a nota'))

if nota < 6.0:

   print('Nota F')
elif nota < 7.0:
    print('Nota D')
elif nota < 8.0:
    print('Nota C')
elif nota < 9.0:
    print('Nota B')
else:
    print('Nota A')
