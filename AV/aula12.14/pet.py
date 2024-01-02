class Pet:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.fome = 0
        self.sede = 0
        self.comida = 100
        #gets
    def get_nome(self):
        return self.nome
    def get_peso(self):
        return self.peso
    def get_fome(self):
        return self.fome
    def get_sede(self):
        return self.sede

       #------------------------------------#
        #sets
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def set_peso(self, novo_peso):
        self.peso = novo_peso

    def set_fome(self, novo_fome):
        self.fome += novo_fome
        while self.fome >= 99:
            print(f'Alimente {self.nome}')
            nova_comida = int(input('Quanto você quer dar de comida para o seu pet? '))
            self.comida -= nova_comida
            self.fome -= novo_fome
    def set_sede(self, nova_sede):
        self.sede += nova_sede

    def imprimir(self):
        print(f'Olá, me chamo {self.nome}')
        print(f'Estou pesando {self.peso} kg')
        print(f'Minha fome está em {self.fome}')
        print(f'Minha sede está em {self.sede}')


caozinho = Pet('Bodo', 15)
caozinho.imprimir()

caozinho.set_fome(10)
caozinho.imprimir()
