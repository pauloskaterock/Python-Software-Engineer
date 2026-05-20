# Você está no Brasil, e para temperatura usamos o grau Celsius.
# Porém, quando você for contrato para trabalhar como programador Python no exterior, deverá usar graus Fahrenheit.

# A fórmula da conversão é a seguinte:

# Tutorial completo de Python
#  Ou seja, você fornece a temperatura em graus Celsius, e seu script faz a conversão para graus Fahrenheit


#conversao para fahrenheit
celsius = float(input('Graus em celsius Cº: '))

F = ((9 / 5) * celsius) + 32

print('{} Cº corresponde à {} Fº'.format(celsius, F))


#conversão para celsius
fahrenheit = float(input(' Graus em fahrenheit Fº '))
C = (fahrenheit - 32) / 1.8
print('{} Fº corresponde à {} Cº'.format(fahrenheit, C))
