# 1. Função soma

def soma(a, b):
    """Esta função retorna a soma de dois números."""
    return a + b

# Exemplo de uso:
resultado = soma(5, 3)
print(resultado)  # Saída: 8


# 2. Função fatorial

def fatorial(n):
    """Esta função calcula o fatorial de um número."""
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Exemplo de uso:
resultado = fatorial(5)
print(resultado)  # Saída: 120


# 3. Função verificar_primo

def verificar_primo(num):
    """Esta função verifica se um número é primo."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Exemplo de uso:
print(verificar_primo(17))  # Saída: True
print(verificar_primo(15))  # Saída: False


# 4. Função inverter_string

def inverter_string(string):
    """Esta função inverte uma string."""
    return string[::-1]

# Exemplo de uso:
resultado = inverter_string("Python")
print(resultado)  # Saída: 'nohtyP'


# 5. Função calcular_media

def calcular_media(*args):
    """Esta função calcula a média de uma lista de números."""
    if not args:
        return 0
    return sum(args) / len(args)

# Exemplo de uso:
media = calcular_media(2, 4, 6, 8)
print(media)  # Saída: 5.0