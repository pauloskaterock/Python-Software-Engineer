# exemplo de como você pode criar um dicionário em Python, junto com uma explicação e alguns exemplos de código:


# Criando um dicionário vazio
meu_dicionario = {}

# Adicionando elementos ao dicionário
meu_dicionario['chave1'] = 'valor1'
meu_dicionario['chave2'] = 'valor2'
meu_dicionario['chave3'] = 'valor3'

# Acessando elementos do dicionário
print(meu_dicionario['chave1'])  # Saída: valor1

# Modificando um valor no dicionário
meu_dicionario['chave2'] = 'novo_valor'

# Removendo um par chave-valor do dicionário
del meu_dicionario['chave3']

# Verificando se uma chave está presente no dicionário
if 'chave1' in meu_dicionario:
    print("A chave 'chave1' está presente no dicionário.")

# Percorrendo o dicionário
for chave, valor in meu_dicionario.items():
    print(f'Chave: {chave}, Valor: {valor}')

# Obtendo todas as chaves do dicionário
chaves = meu_dicionario.keys()
print("Chaves:", chaves)

# Obtendo todos os valores do dicionário
valores = meu_dicionario.values()
print("Valores:", valores)

# Obtendo o comprimento do dicionário
print("Comprimento:", len(meu_dicionario))

# Limpando o dicionário
meu_dicionario.clear()
print("Dicionário após limpar:", meu_dicionario)



# Explicação:

# Um dicionário em Python é uma estrutura de dados que mapeia chaves a valores. É semelhante a uma lista, mas em vez de índices numéricos, os dicionários permitem usar chaves de qualquer tipo imutável (como strings, tuplas ou números).

# Você pode criar um dicionário vazio usando {} ou dict().

# Para adicionar um par chave-valor ao dicionário, você usa a sintaxe dicionario[chave] = valor.

# Para acessar um valor no dicionário, você utiliza dicionario[chave].

# Para modificar um valor, basta atribuir um novo valor à chave desejada.

# Para remover um par chave-valor, você pode usar o operador del.

# Você pode verificar se uma chave está presente em um dicionário usando in.

# Para iterar sobre um dicionário, você pode usar um loop for com items(), que retorna pares chave-valor.

# keys() retorna uma lista de todas as chaves do dicionário, enquanto values() retorna uma lista de todos os valores.

# len() retorna o número de pares chave-valor no dicionário.

# clear() remove todos os itens do dicionário.





