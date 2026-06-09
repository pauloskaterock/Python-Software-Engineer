# Escreva um script em Python que pergunta o preço de um produto e mostre:
# Preço original
# Desconto em porcentagem
# Valor do desconto
# Preço com o desconto

# O desconto quem define é o gerente, na forma de variável global.



desc = 10 # 10%

def desconto(valor):
    global desc
    print("Preço original   : R$ ",valor)
    print("Desconto         : ", desc,"%")

    desc /= 100
    print("Valor desconto   : ", valor*desc)
    print("Preço c/ desconto: ", valor*(1-desc) )

val = float(input("Preço do produto: "))
desconto(val)



# -------------------------------------------------

# Crie um programa em Python que peça o raio de uma circunferência ao usuário, em seguida exiba o perímetro e a área desse círculo.

# Inicialmente, vamos definir uma variável global, uma constante, o valor de pi, que é 3,14

# Depois, criamos a função de perímetro (2 x pi x raio) e a de área (pi x raio²).
# Bem simples, veja:


pi = 3.14

def perimetro(raio):
    print("Perimetro: ", 2*pi*raio)

def area(raio):
    print("Área: ", pi*raio*raio)

raio = float(input("Raio do círculo: "))
perimetro(raio)
area(raio)
