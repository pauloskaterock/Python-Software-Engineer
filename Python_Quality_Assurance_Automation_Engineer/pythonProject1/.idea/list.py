# 1. Lista Simples
# Uma lista simples é uma sequência ordenada de itens separados por vírgulas, e é definida utilizando colchetes [].

# Exemplo de Código:

lista_simples = [1, 2, 3, 4, 5]
print(lista_simples)


# 2. Lista de Listas (Lista Aninhada)
# Uma lista de listas é uma lista que contém outras listas como seus elementos. Pode-se pensar nisso como uma matriz multidimensional.

# Exemplo de Código:


lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lista_aninhada)


# 3. Lista Vazia
# Uma lista vazia é uma lista que não contém nenhum elemento.

# Exemplo de Código:


lista_vazia = []
print(lista_vazia)


# 4. Acessando Elementos da Lista
# Os elementos de uma lista podem ser acessados pelo seu índice, que começa em 0.

# Exemplo de Código:


lista = [1, 2, 3, 4, 5]
print(lista[0])  # Saída: 1
print(lista[2])  # Saída: 3


# 5. Adicionando Elementos à Lista
# Elementos podem ser adicionados a uma lista utilizando o método append().

# Exemplo de Código:

lista = [1, 2, 3]
lista.append(4)
print(lista)  # Saída: [1, 2, 3, 4]

# 6. Removendo Elementos da Lista
# Elementos podem ser removidos de uma lista utilizando o método remove() ou pop().

# Exemplo de Código:


lista = [1, 2, 3, 4]
lista.remove(3)
print(lista)  # Saída: [1, 2, 4]

item_removido = lista.pop(1)
print(item_removido)  # Saída: 2
print(lista)  # Saída: [1, 4]


# 7. Iterando sobre uma Lista
# Pode-se iterar sobre os elementos de uma lista utilizando um loop for.

# Exemplo de Código:


lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)


# 8. Comprimento da Lista
# O comprimento de uma lista (ou seja, o número de elementos que ela contém) pode ser obtido utilizando a função len().

# Exemplo de Código:


lista = [1, 2, 3, 4, 5]
print(len(lista))  # Saída: 5


# Esses são alguns dos conceitos básicos de listas em Python. Elas são uma estrutura de dados extremamente versátil e útil em programação Python.





