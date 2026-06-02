# Exercício 02 resolvido
# Agora, não sabemos o valor do desconto de cada produto.
# Então, além de perguntar o valor original do produto, também temos que perguntar o valor do desconto e armazenar numa variável chamada 'desconto'.

# Mas aqui que mora o perigo.
# Quem vai fornecer o valor do desconto vai fornecer em porcentagem.

# Tipo, vai escrever '10' para 10%. Porém na hora de dar o desconto, a gente multiplica por 0.10 e não por 10.



# Então, o que fazer? Simples: pegamos o valor que a pessoa vai digitar e dividimos por 100 (porcentagem = por cem tagem).

# Aqui temos o pulo do gato.
# Temos a variável 'desconto' com valor 10.
# Como transformar ela pra ter o valor 0.1 armazenado?

# Pode declarar uma nova variável, a desconto2, que é:
# desconto2 = desconto / 100

# Ou mais comum em programação:
# desconto = desconto / 100

# Isso quer dizer o seguinte: "Python, o novo valor de desconto é o valor antigo dela dividido por 100".

# O valor que a pessoa ganha de desconto é o valor original multiplicado por essa variável desconto.

# E o novo valor, incluído o desconto?
# Se 10% é o desconto, então o valor com desconto incluso é: valor original multiplicado por 0.9 (de 90% = 100% - 10%)

# Basta fazer: 1 - desconto
# Se o desconto é 0.3 , então vamos multiplicar o valor original por: 1 - 0.3 = 0.7

# Em código Python, fica assim: valor_original * (1 - desconto)

# O código final fica:




# Vamos pedir o valor original do produto
valor_original = float( input("Valor original: R$ ") )

# Desconto que será concedido
desconto = float( input("Desconto (em %) para esse produto: ") )

# Transformando a porcentagem em número decimal
desconto = desconto / 100

# Exibindo tudo
print('Valor original:     R$', valor_original)
print('Desconto ganho:     R$', valor_original * desconto)
print('Valor com desconto: R$', valor_original * (1-desconto) )