numero = 10
texto ="charles"
verdade = True 

print('Numero: '+str(numero), f'Texto: {texto}' , f"Verdade: {str(verdade)}")

# print(type(numero) ,type(texto) ,type(verdade))

#######################################################################################################

# Python, há várias maneiras de concatenar strings e outros tipos de dados. Aqui estão algumas das mais comuns:

# 1. Operador +
# O operador + é a maneira mais simples de concatenar duas ou mais strings.


# str1 = "Olá"
# str2 = "Mundo"
# resultado = str1 + " " + str2
# print(resultado)  # Output: Olá Mundo
# 2. join() Método
# O método join() é eficiente para concatenar uma sequência de strings.


# partes = ["Olá", "Mundo"]
# resultado = " ".join(partes)
# print(resultado)  # Output: Olá Mundo
# 3. format() Método
# O método format() permite inserir variáveis em uma string template.


# str1 = "Olá"
# str2 = "Mundo"
# resultado = "{} {}".format(str1, str2)
# print(resultado)  # Output: Olá Mundo
# 4. f-strings (Python 3.6+)
# f-strings são uma maneira moderna e concisa de formatar strings.


# str1 = "Olá"
# str2 = "Mundo"
# resultado = f"{str1} {str2}"
# print(resultado)  # Output: Olá Mundo
# 5. += Operador
# O operador += adiciona uma string ao final de outra string existente.


# resultado = "Olá"
# resultado += " "
# resultado += "Mundo"
# print(resultado)  # Output: Olá Mundo
# 6. Usando * para repetição de strings
# Embora não seja exatamente concatenação, você pode repetir uma string várias vezes usando o operador *.


# str1 = "Olá"
# resultado = str1 * 3
# print(resultado)  # Output: OláOláOlá
# 7. Concatenando outros tipos de dados
# Para concatenar tipos de dados diferentes, como strings e números, você geralmente precisa converter os números em strings primeiro.


# str1 = "O número é "
# num = 42
# resultado = str1 + str(num)
# print(resultado)  # Output: O número é 42
# Ou usando f-strings:


# str1 = "O número é"
# num = 42
# resultado = f"{str1} {num}"
# print(resultado)  # Output: O número é 42