# Em Python, as condicionais são usadas para executar blocos de código diferentes com base em certas condições. Aqui estão alguns exemplos de como usar condicionais em Python:

# 1. Estrutura if
# A estrutura if executa um bloco de código se a condição for verdadeira.


# x = 10
# if x > 5:
#     print("x é maior que 5")
# # Output: x é maior que 5
# 2. Estrutura if-else
# A estrutura if-else executa um bloco de código se a condição for verdadeira e outro bloco se a condição for falsa.

# x = 3
# if x > 5:
#     print("x é maior que 5")
# else:
#     print("x não é maior que 5")
# # Output: x não é maior que 5
# 3. Estrutura if-elif-else
# A estrutura if-elif-else permite verificar múltiplas condições.


# x = 7
# if x > 10:
#     print("x é maior que 10")
# elif x > 5:
#     print("x é maior que 5, mas menor ou igual a 10")
# else:
#     print("x é menor ou igual a 5")
# # Output: x é maior que 5, mas menor ou igual a 10
# 4. Condicional aninhada
# As condicionais podem ser aninhadas, ou seja, uma estrutura condicional pode estar dentro de outra.


# x = 15
# if x > 10:
#     print("x é maior que 10")
#     if x > 20:
#         print("x é maior que 20")
#     else:
#         print("x é menor ou igual a 20")
# else:
#     print("x é 10 ou menor")
# # Output:
# # x é maior que 10
# # x é menor ou igual a 20
# 5. Operadores lógicos
# Você pode usar operadores lógicos (and, or, not) para combinar múltiplas condições.


# x = 8
# if x > 5 and x < 10:
#     print("x está entre 5 e 10")
# # Output: x está entre 5 e 10

# y = 3
# if y < 5 or y > 10:
#     print("y é menor que 5 ou maior que 10")
# # Output: y é menor que 5 ou maior que 10

# z = 5
# if not z == 5:
#     print("z não é igual a 5")
# else:
#     print("z é igual a 5")
# # Output: z é igual a 5
# 6. Condicional ternária
# A condicional ternária é uma forma concisa de expressar uma condição if-else em uma única linha.


# x = 5
# resultado = "Maior que 10" if x > 10 else "10 ou menor"
# print(resultado)
# # Output: 10 ou menor
# 7. Usando in com condicionais
# O operador in verifica se um valor está presente em uma sequência, como uma lista, tupla ou string.


# fruta = "maçã"
# if fruta in ["maçã", "banana", "laranja"]:
#     print(f"{fruta} está na lista de frutas")
# # Output: maçã está na lista de frutas

# -----------------------------------------------------------------------------

# numero = 10
# texto ="charles"
# verdade = True 

# if texto == 'charles':
#     print(texto)
#     print(verdade)

# else:
#     texto == 'pedro'
#     numero = 12
#     print(texto)
#     print(verdade)

# -----------------------------------------------------------------

# funcionarios = ['pedro', 'maria', 'joao']

# for item in funcionarios:
#     print(item[0])

# ---------------------------------------------------------------
# numero = 10
# texto ="charles"
# verdade = True 

# while numero <= 20:
#     print(numero)
#     numero = numero + 1

# ------------------------------------------------------------

numero = 10
texto ="charles"
verdade = True 

def frase():
    print('curso de RPA')


#frase()

def calculaNumero(num1 , num2):
    resultado = num1 + num2
    #print(resultado)
    return resultado


valor = calculaNumero(2 , 5)



print(valor)


