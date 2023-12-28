class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    def nome(self):
        return self.__nome
    def ferramenta(self):
        return self.__ferramenta
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta: 
    def __init__(self, marca):
        self.__marca = marca
    def marca(self):
        return self.__marca
    def escrever(self):
        print('Caneta está escrevendo')

class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina está escrevendo')

escritor = Escritor('jp Lovecraft')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
escritor.ferramenta = maquina #fazendo a associação
escritor.ferramenta.escrever() #acessando o metodo da associada