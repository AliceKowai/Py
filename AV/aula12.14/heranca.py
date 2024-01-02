class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclass = self.__class__.__name__
    def fala(self):
        print('Falando')
class Cliente(Pessoa):
    def comprar(self):
        print(f'comprando')
class Aluno(Pessoa):
    def comprar(self):
        print(f'Estudando')


c1 = Cliente('Luiz', 45)
print(c1.nome)
a1 = Aluno('Maria', 54)
print(a1.nome)