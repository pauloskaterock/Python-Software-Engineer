# Tarefa é criar um programa envolvendo a poupança.
# Você vai perguntar o valor inicial investido na poupança, a rentabilidade mensal, quantos meses o cliente deseja deixar o dinheiro investido e mostrar o valor final na conta do cliente do banco

#pergunta valor inicial
# valor_inicial = float( input("Valor inicial investido na poupança: R$ ") )

# #pergunta a rentabilidade
# rentabilidade_mensal = float( input("rentabilidade_mensal: R$ ") )


# valor_inicial = rentabilidade_mensal / 100

# quantidade_meses = int( input("quantidade_meses: "))


# valor_final = valor_inicial * (1 + rentabilidade_mensal / 100) ** quantidade_meses


# print('Valor final na conta: R$ ', valor_final)



#--------------------------------------------------------------

# Um cliente pediu que o sistema do banco tivesse a seguinte função:
# Dizer o valor inicial que ele deve investir, para ao final de 'm' meses ele tenha um valor 'vf', supondo que este dinheiro esteja rendendo uma rentabilidade 'i' mensal, em porcentagem esse 'i'.

# Faça um programa que pede o valor final, o tanto de meses que vai ficar aplicado, a rentabilidade e o script mostre o valor inicial que ele deve investir para atingir tal objetivo.


valor_investido = float( input("Valor  investido na poupança: R$ ") )
quantos_meses_investido = float( input("Meses que o cliente gostaria de investir: R$ ") )
rentabilidade = float( input("Rentabilidade: "))

rentabilidade_final = rentabilidade/ 100

valor_final = valor_investido/ ((1 + rentabilidade) ** quantos_meses_investido)


print('Valor final na conta: R$ ', valor_final)
