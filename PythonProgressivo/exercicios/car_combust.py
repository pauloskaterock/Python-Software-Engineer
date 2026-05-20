# Um novo modelo de carro, super econômico foi lançado.
# Ele faz 20 km com 1 litro de combustível.
# Cada litro de combustível custa R$ 5,00.

# Faça um programa que pergunte ao usuário quanto de dinheiro ele tem e em seguida diga quantos litros de combustível ele pode comprar e quantos kilometros o carro consegue andar com este tanto de combustível


quantidade_dinheiro = float(input('Quanto de grana o malandro tem: '))
litros_combustivel = quantidade_dinheiro / 5.0
kilometros = litros_combustivel * 20

print(f'Com R$ {quantidade_dinheiro:.2f}, você pode comprar {litros_combustivel:.2f} litros de combustível.')
print(f'Com {litros_combustivel:.2f} litros, o carro consegue andar {kilometros:.2f} km.')
