# Sua primeira tarefa é criar um programa em Python que pede o preço original de um produto e dá 20% de desconto.

# Você deve mostrar uma tabela contendo:
# Preço original do produto
# Valor do desconto em R$ (tipo 'Você ganho R$ xx,xx de desconto')
# Valor do produto com o desconto


# Vamos pedir o valor original do produto
valor_original = float( input("Valor original: R$ ") )

# Desconto ganho de 20%
valor_descontado = valor_original * 0.2

# Valor com desconto incluso
novo_valor = valor_original * 0.80

# Exibindo tudo
print('Valor original:     R$', valor_original)
print('Desconto ganho:     R$', valor_descontado)
print('Valor com desconto: R$', novo_valor)