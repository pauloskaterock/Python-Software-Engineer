# Herança em Python:
# A herança é um conceito fundamental na programação orientada a objetos, onde uma classe (subclasse) pode herdar atributos e métodos de outra classe (superclasse). Isso permite a reutilização de código e a criação de uma hierarquia de classes.

# Exemplo de código:


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):  # Dog herda da classe Animal
    def make_sound(self):
        return "Woof!"

class Cat(Animal):  # Cat herda da classe Animal
    def make_sound(self):
        return "Meow!"

dog = Dog("Buddy")
print(dog.name)          # Saída: Buddy
print(dog.make_sound())  # Saída: Woof!

cat = Cat("Whiskers")
print(cat.name)          # Saída: Whiskers
print(cat.make_sound())  # Saída: Meow!