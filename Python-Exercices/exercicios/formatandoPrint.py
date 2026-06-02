# Você foi contratado pela Caixa Econômica Federal para atualizar seu sistema.
# Como primeira tarefa, você vai criar um script que diga quanto cada ganhador da Mega-Sena vai receber, ao ter o prêmio dividido com outros ganhadores.

print("----------------------------------------")

# # Prêmio da Mega-Sena
# total = float( input('Premio total da Mega: ') )

# # Número de ganhadores
# num = int( input('Numero de ganhadores: ') )

# print('Cada um vai ficar com R$ ', (total/num) )

print("----------------------------------------")


# Prêmio da Mega-Sena
total = float( input('Premio total da Mega: ') )

# Número de ganhadores
num = int( input('Numero de ganhadores: ') )

print('O premio total foi R$%.2f para %d ganhadores, onde cada um ficou \
com R$%.2f' %(total,num,total/num))