# Os loops em Python são estruturas de controle que permitem repetir um bloco de código várias vezes. Existem dois tipos principais de loops em Python: for e while. Aqui estão exemplos e explicações para ambos:

# Loop for:
# O loop for é usado para iterar sobre uma sequência (como uma lista, tupla, conjunto ou string) ou qualquer iterável em Python.

# Exemplo:



# Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

# Iterando sobre uma string
for letra in "Python":
    print(letra)

# Iterando sobre um intervalo de números
for i in range(5):
    print(i)


# Explicação:


# O loop for começa com a palavra-chave for, seguida por uma variável de iteração (como fruta ou letra), seguida pela palavra-chave in, e depois a sequência ou iterável a ser iterado (como frutas, "Python", ou range(5)).
# Dentro do loop, o bloco de código indentado é executado para cada elemento da sequência ou iterável.
# Loop while:
# O loop while é usado para repetir um bloco de código enquanto uma condição específica for verdadeira.

# Exemplo:

# Imprimindo números de 0 a 4 usando um loop while
    

contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Loop while com entrada do usuário
resposta = ""
while resposta != "parar":
    resposta = input("Digite 'parar' para encerrar: ")
    print("Você digitou:", resposta)

# Explicação:


# O loop while começa com a palavra-chave while, seguida por uma condição (como contador < 5 ou resposta != "parar").
# O bloco de código indentado é executado repetidamente enquanto a condição especificada for verdadeira.
# É importante garantir que a condição eventualmente se torne falsa, caso contrário, o loop continuará para sempre, resultando em um loop infinito.
# Os loops são uma parte fundamental da programação em Python e são amplamente utilizados para automatizar tarefas repetitivas e processar coleções de dados. Certifique-se de compreender bem como funcionam para utilizar essa poderosa ferramenta de forma eficaz em seus programas.