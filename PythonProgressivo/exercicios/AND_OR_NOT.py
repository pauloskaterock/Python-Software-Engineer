# Para votar, você deve ter entre 18 anos e menos de 65 anos.
# Escreva um programa que pergunte sua idade e diga se você é obrigado a votar ou não.

# Temos dois testes:
# Testar se tem 18 anos ou mais
# Testar se tem 65 ou menos

# Para votar, cada um dos testes deve ser TRUE.
# O nosso código fica:



resposta=int( input('Qual sua idade: ') )

if resposta>=18 and resposta <=65:
    print('Você é obrigado a votar!')
else:
    print('Você não é obrigado a votar')



# --------------------------------------------------------------------------

# Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. Escreva um programa que pergunta a situação do usuário (se é idoso, se é gestante, se é cadeirante ou nenhum destes) e diga se ele pode ter acesso a fila prioridade ou não.

# Para o usuário ter acesso a fila de prioridade, ele deve ser idoso OU gestante OU cadeirante. Qualquer um desses. Basta que uma dessas condições seja verdadeira, para o teste condicional ser verdadeiro.


print('1. Idoso')
print('2. Gestante')
print('3. Cadeirante')
print('4. Nenhum destes')
resposta=int( input('Você é: ') )

if (resposta==1) or (resposta==2) or (resposta==3) :
    print('Você tem direito a fila prioritária')
else:
    print('Você não tem direito a nada. Vá pra fila e fique quieto')



# skate jam session old scholl
# master 35
# legend 40
# gran legend 50
# master_legend 60

print('35. master')
print('40. legend')
print('50. gran legend')
print('60. master_legend')

resposta=int( input('Você é: ') )

if (resposta==35) or (resposta==40) or (resposta==50) or (resposta==60) :
    print('Você é old school')
else:
    print('Você não tem direito a nada. Vá pra fila e fique quieto')


# --------------------------------------------------------


# Operador NOT em Python


banda = input('Qual melhor banda do mundo? ')

if not banda=='rush':
    print('Herege!')
else:
    print('Correto, é o Rush!')



# --------------- Exercicios ----------------------------------------

# 1. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

char=input('Digite um caractere: ')

if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or \
  char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
    print('Vogal')
else:
    print('Consoante')


# -------------------------------------

# Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:

#     A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;


#     A mensagem "Reprovado", se a média for menor do que sete;

#     A mensagem "Aprovado com Distinção", se a média for igual a dez.


nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2
print('Media: ',media)

if media<7.0:
  print('Reprovado')
elif media<10:
  print('Aprovado')
else:
  print('Aprovado com Distinção!')


# --------------------------------------------------------------


# 3. Faça um Programa que leia três números inteiros e mostre o maior deles.
primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

maior = primeiro

if (segundo > maior):
        maior = segundo
if (terceiro > maior):
        maior = terceiro

print('Maior: ',maior)

# ---------------------------------------------------


# 5. Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela


num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

# Trocando os valores
num1, num2 = num2, num1

print('Após a troca:')
print('Primeiro número:', num1)
print('Segundo número:', num2)


# ---------------------------------------------------


# 6. Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

# Ordenando os números em ordem decrescente
if num1 >= num2 and num1 >= num3:
    maior = num1
    if num2 >= num3:
        medio = num2
        menor = num3
    else:
        medio = num3
        menor = num2
elif num2 >= num1 and num2 >= num3:
    maior = num2
    if num1 >= num3:
        medio = num1
        menor = num3
    else:
        medio = num3
        menor = num1
else:
    maior = num3
    if num1 >= num2:
        medio = num1
        menor = num2
    else:
        medio = num2
        menor = num1

print('Números em ordem decrescente:')
print(maior)
print(medio)
print(menor)

# ------------------------------------------------------------------


# 7. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


turno = input('Em que turno você estuda? (M/V/N): ')

if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')

# -------------------------------------------------------------


# 8. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.



# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:


  # salários até R$ 280,00 (incluindo) : aumento de 20%
  #   salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
  #   salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
  #   salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
  #   o salário antes do reajuste;
  #   o percentual de aumento aplicado;
  #   o valor do aumento;
  #   o novo salário, após o aumento.
