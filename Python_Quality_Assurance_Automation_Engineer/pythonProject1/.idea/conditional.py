# # As condicionais em Python são usadas para tomar decisões com base em condições específicas. A estrutura básica de uma condicional em Python é a seguinte:


# if condição:
#     # código a ser executado se a condição for verdadeira
# else:
#     # código a ser executado se a condição for falsa
# Além disso, Python permite o uso de outras construções como elif (abreviação de "else if") para adicionar mais condições intermediárias. Aqui está a estrutura completa:


# if condição_1:
#     # código a ser executado se condição_1 for verdadeira
# elif condição_2:
#     # código a ser executado se condição_1 for falsa e condição_2 for verdadeira
# else:
#     # código a ser executado se nenhuma das condições anteriores for verdadeira


# # Aqui estão alguns exemplos de condicionais em Python com explicações:

# # Exemplo 1: Verificação de idade para acesso a um site


# idade = int(input("Qual é a sua idade? "))

# if idade >= 18:
#     print("Você é maior de idade. Bem-vindo ao site.")
# else:
    
#     print("Você é menor de idade. Você não tem permissão para acessar este site.")


# # Neste exemplo, o programa verifica se a idade inserida pelo usuário é maior ou igual a 18. Se for, imprime uma mensagem de boas-vindas, caso contrário, informa que o acesso não é permitido.

# # Exemplo 2: Classificação de um número como positivo, negativo ou zero
    

# numero = float(input("Digite um número: "))

# if numero > 0:
#     print("O número é positivo.")
# elif numero < 0:
#     print("O número é negativo.")
# else:
#     print("O número é zero.")

# # Neste exemplo, o programa verifica se o número inserido é maior que zero, menor que zero ou igual a zero e imprime uma mensagem correspondente.

# # Exemplo 3: Verificação de número par ou ímpar


# numero = int(input("Digite um número: "))

# if numero % 2 == 0:
#     print("O número é par.")
# else:
#     print("O número é ímpar.")


# # Neste exemplo, o programa verifica se o número inserido é divisível por 2 (ou seja, se o resto da divisão por 2 é igual a zero) e imprime uma mensagem correspondente.