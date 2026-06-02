# Polimorfismo em Python:
# O polimorfismo é a capacidade de um objeto poder ser tratado de várias maneiras diferentes. Em Python, isso é alcançado através do conceito de métodos com o mesmo nome em classes diferentes, que podem ser chamados de maneira uniforme, mas que executam comportamentos diferentes dependendo da classe do objeto.

# Exemplo de código:

class Bird:
    def sound(self):
        return "Chirp"

class Dog:
    def sound(self):
        return "Woof"

def make_sound(animal):
    return animal.sound()

bird = Bird()
dog = Dog()

print(make_sound(bird))  # Saída: Chirp
print(make_sound(dog))   # Saída: Woof