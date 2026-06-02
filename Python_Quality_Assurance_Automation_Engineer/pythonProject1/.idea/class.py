# Vou criar uma classe simples em Python com uma explicação detalhada e alguns exemplos de código. Vamos criar uma classe chamada Carro que representa um veículo básico. Esta classe terá atributos como marca, modelo, cor e métodos para acelerar, frear e obter informações sobre o carro.


class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        if self.velocidade - decremento >= 0:
            self.velocidade -= decremento
        else:
            self.velocidade = 0

    def info(self):
        return f"Carro: {self.marca} {self.modelo}, Cor: {self.cor}, Velocidade: {self.velocidade} km/h"


# Exemplo de utilização da classe Carro
if __name__ == "__main__":
    # Criando um objeto da classe Carro
    meu_carro = Carro("Toyota", "Corolla", "Prata")

    # Imprimindo informações iniciais do carro
    print(meu_carro.info())  # Saída: Carro: Toyota Corolla, Cor: Prata, Velocidade: 0 km/h

    # Acelerando o carro em 50 km/h
    meu_carro.acelerar(50)
    print(meu_carro.info())  # Saída: Carro: Toyota Corolla, Cor: Prata, Velocidade: 50 km/h

    # Freando o carro em 20 km/h
    meu_carro.frear(20)
    print(meu_carro.info())  # Saída: Carro: Toyota Corolla, Cor: Prata, Velocidade: 30 km/h

# Explicação:

# Definição da Classe: class Carro: inicia a definição da classe Carro.

# Método __init__: Este é o método especial __init__, também conhecido como construtor. Ele é chamado automaticamente quando um novo objeto é criado a partir da classe. Aqui, definimos os atributos iniciais do carro, como marca, modelo, cor e velocidade inicial.

# Métodos de Instância (acelerar, frear, info): Esses são os métodos que operam nos objetos criados a partir da classe Carro. acelerar aumenta a velocidade do carro, frear diminui a velocidade (mas não pode ser negativa), e info retorna uma string formatada com as informações do carro.

# Método info: Este método retorna uma string formatada contendo informações sobre o carro, incluindo marca, modelo, cor e velocidade atual.

# Exemplo de Utilização: No bloco if __name__ == "__main__":, criamos um objeto meu_carro da classe Carro e demonstramos como usar os métodos acelerar e frear, seguido pela impressão das informações do carro usando o método info.







