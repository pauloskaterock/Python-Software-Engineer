# 01. Escreva um programa que pede o raio de um círculo, e em seguida exiba o perímetro e área do círculo.

# Para saber o valor do pi, faça:

import math

# print(math.pi)

raio = 3.14
perimetro = 2 * math.pi * raio
area = math.pi * raio ** 2

print(f" O perímetro do círculo é:{perimetro}")
print(f"A área do círculo é: {area}")
