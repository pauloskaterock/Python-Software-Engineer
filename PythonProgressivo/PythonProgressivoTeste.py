# # print ('Ola python')


# # Crie um programa que exiba na tela seu nome completo, sua cidade, estado e data de nascimento.

# print('Paulinho Robotics Python Automation Engineer')
# nome = 'Paulinho'
# idade = 38
# cidade = 'dirtyMaua'
# estado = 'sp'
# nascimento = 1988

# print('Seu nome é:', nome)
# print('Sua idade é:', idade)
# print('Sua cidade é:', cidade)
# print('Seu estado é:', estado)
# print('Sua data de nascimento é:', nascimento)


# #-------------------------------------------------------------------------

# # Crie um programa que exiba na tela o texto 'A melhor banda do mundo é [nome da banda] e a melhor música é [nome da música]'.

# band = 'zumbis do espaço'
# musica = 'chamado da estrada'

# print('A melhor banda do mundo é' , band,  ' e a melhor música é ', musica)


# #---------------------------------------------------------------------------

# salario=0.0
# print('Antes de ser programdor eu ganhava R$',salario,'por mes')

# salario=5000.0
# print('Agora virei programador Python e ganho R$',salario)

# #-------------------------------------------------------------------------

# # Exercício: O seguinte código imprime todas as palavras reservadas (keywords) do Python, rode ele e escreva nos comentários o resultado:

# import keyword
# print(keyword.kwlist)

# #---------------------------------------------------------------------------

# idade=input('Qual sua idade? ')
# nome=input('Qual seu nome? ')

# print('Olá, seu nome é ', nome, ' e tem ', idade, ' anos de idade! Seja bem vindo ao Curso Python Progressivo')
# #--------------------------------------------------------------------
# string=input("Digite uma string: ")
# print( type(string) )

# inteiro=input("Digite um inteiro: ")
# print( type(inteiro) )

# decimal=input("Digite um float: ")
# print( type(decimal) )



# var1 = '2112'
# print(type())

# var2 = int(var1)
# print( type(var2) )




# var1=input("Digite um decimal: ")
# print( type(var1) )

# var2=float(var1)
# print( type(var2) )

# var3=2112
# var4=float(var3)

# print( type(var4) )

# print(var4)


# var1 = int( input("Digite um inteiro: ") )
#------------------------------------------------------------------------
# var1 = int( input("Digite um inteiro: ") )
# var2 = int( input("Digite outro inteiro: ") )

# produto = var1 ** var2

# print(produto)


# --------------------------------------------


var = input('digite algo')
print('voce digitou', var)



# ---------------------------------------------------

# tenho que estudar python 2 horas ou 120 minutos
# crie um programa que calcule quantos blocos de 40 minutos devo usar para chegara 120 minutos de estudo


# estu1 = 40
# estu2 = 40
# estu3 = 40

# estuFinal = estu1 + estu2 + estu3
# print("O total de minutos de estudo é:", estuFinal)

#-----------------------------------------------------

# Prêmio da Mega-Sena
# total = float( input('Premio total da Mega: ') )

# # Número de ganhadores
# num = int( input('Numero de ganhadores: ') )

# print('Cada um vai ficar com R$ ', (total/num) )
# print('Cada um vai ficar com R$ %.2f' % (total/num) )

# print('O premio total foi R$%.2f para %d ganhadores, onde cada um ficou \
# com R$%.2f' %(total,num,total/num))

#-----------------------------------------------------------
bru = input('She is hot')
gab = input('she is hot')

if bru == gab:
  print(' Ambos are hot')

elif bru != gab:
  print('Not equal')
