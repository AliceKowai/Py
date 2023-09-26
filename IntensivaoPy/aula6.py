import os
carros = []


class Carro:
    nome = ""
    pot = 0
    velMax = False
    ligado = False

    def __init__(self, nome, pot):
        self.nome = nome
        self.pot = pot
        self.velMax = int(pot) * 2
        self.ligado = False
    
    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False
    
    def info(self):
        print("Nome: ", self.nome)
        print("Potencia: ", self.pot)
        print("velocidade maxima: ", self.velMax)
        print("Ligado: ", ("sim" if self.ligado == True else "não"))

    @staticmethod
    def Menu():
        os.system("cls") or None
        print("1 - Novo Carro")
        print("2 - Informações do Carro")
        print("3 - Exluir Carro")
        print("4 - Ligar Carro")
        print("5 - Desligar Carro")
        print("6 - Listar Carro")
        print("7 - Sair")
        print("Quantidade de carros: ", len(carros))
        opc = input("Digite uma opção: ")
        return opc

    @staticmethod
    def NovoCarro():
        os.system("cls") or None
        n = input("Nome do Carro: ")
        p = input("Potencia do carro: ")
        car = Carro(n, p)
        carros.append(car)
        print("Novo Carro Criado")
        os.system("pause")

    @staticmethod
    def informacoes():
        os.system("cls") or None
        n = input("Informe o número do carro que deseja ver as informações: ")
        try:
            carros[int(n)].info()
        except IndexError:
            print("Carro não existe na lista")
        os.system("pause")

    @staticmethod
    def excluirCarro():
        os.system("cls") or None
        n = input("Informe o número do carro que deseja excluir: ")
        try:
            del carros[int(n)]
        except IndexError:
            print("Carro não existe na lista")
        os.system("pause")

    @staticmethod
    def ligarCarro():
        os.system("cls") or None
        n = input("Informe o número do carro que deseja ligar: ")
        try:
            carros[int(n)].ligar()
        except IndexError:
            print("Carro não existe na lista")
        os.system("pause")

    @staticmethod
    def desligarCarro():
        os.system("cls") or None
        n = input("Informe o número do carro que deseja desligar: ")
        try:
            carros[int(n)].desligar()
        except IndexError:
            print("Carro não existe na lista")
        os.system("pause")

    @staticmethod
    def listarCarro():
        os.system("cls") or None
        p = 0
        for c in carros:
            print(str(p), " - ", c.nome)
            p = p + 1
        os.system("pause")


ret = Carro.Menu()
while ret < "7":
    if ret == "1":
        Carro.NovoCarro()
    elif ret == "2":
        Carro.informacoes()
    elif ret == "3":
        Carro.excluirCarro()
    elif ret == "4":
        Carro.ligarCarro()
    elif ret == "5":
        Carro.desligarCarro()
    elif ret == "6":
        Carro.listarCarro()
    ret = Carro.Menu()

os.system("cls") or None
print("Programa finalizado")
