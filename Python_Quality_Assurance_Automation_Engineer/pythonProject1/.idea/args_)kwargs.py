# Em Python, *args e **kwargs são usados para lidar com um número variável de argumentos em funções. Eles permitem que você passe um número arbitrário de argumentos posicionais e de palavra-chave para uma função, o que pode ser útil em situações onde o número de argumentos não é conhecido antecipadamente.

# *args:
# *args é usado para passar um número variável de argumentos posicionais para uma função.
# *args é uma tupla contendo todos os argumentos posicionais que foram passados para a função.
# O operador * é colocado antes do parâmetro que você deseja que aceite múltiplos argumentos posicionais.
# Você pode usar qualquer nome para o parâmetro, mas args é uma convenção comum.

# Exemplo de código:



def soma(*args):
    total = 0
    for num in args:
        total += num
    return total

print(soma(1, 2, 3, 4))  # Saída: 10


# **kwargs:
# **kwargs é usado para passar um número variável de argumentos de palavra-chave para uma função.
# **kwargs é um dicionário contendo todos os argumentos de palavra-chave que foram passados para a função.
# O operador ** é colocado antes do parâmetro que você deseja que aceite múltiplos argumentos de palavra-chave.
# Você pode usar qualquer nome para o parâmetro, mas kwargs é uma convenção comum.


# Exemplo de código:

def mostrar_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

mostrar_info(nome='João', idade=30, cidade='São Paulo')
# Saída:
# nome: João
# idade: 30
# cidade: São Paulo


# Em resumo, *args e **kwargs são úteis quando você precisa lidar com um número variável de argumentos em suas funções, tornando suas funções mais flexíveis e genéricas.





