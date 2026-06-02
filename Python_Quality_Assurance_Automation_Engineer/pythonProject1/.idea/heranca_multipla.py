# Herança Múltipla em Python:
# A herança múltipla é um conceito onde uma classe pode herdar atributos e métodos de mais de uma classe pai. Em Python, uma classe pode herdar de várias classes usando uma lista de classes pai.

# Exemplo de código:


class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):  # Herda de A e B
    def method_c(self):
        print("Method C")

obj = C()
obj.method_a()  # Saída: Method A
obj.method_b()  # Saída: Method B
obj.method_c()  # Saída: Method C