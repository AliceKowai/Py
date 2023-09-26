## classes ##

class Anime:
    ep=0
    bom=False
    genero=""

Naruto=Anime()
snk=Anime()
beserk=Anime()

Naruto.bom=True
Naruto.genero="shonen"
Naruto.ep=220

print("Genero do Naruto é ",Naruto.genero)

## Construtor ##

class Anime:
    nome=""
    ep=0
    bom=False
    genero=""
    def __init__(self,nome,ep,bom,genero):
        self.nome=nome
        self.ep=ep
        self.bom=bom
        self.genero=genero
    def mostrar(self):
        print("Nome: ", self.nome)
        print("Número de episodios: ", self.ep)
        print("Genero do anime: ", self.genero)
        bom="Sim" if self.bom else "Não"
        print("O anime é bom?", bom )
        print("***************************")

yamada_kun_lvl_999=Anime("Yamada-kun lvl999",13,True,"shoujo")
mirai_nikki=Anime("Mirai Nikki",26,False,"shonen")

yamada_kun_lvl_999.mostrar()
mirai_nikki.mostrar()


## Heranças de classe ##
class NPC:
    def __init__(self, nome, time, forca, municao):
        self.nome=nome
        self.time=time
        self.forca=forca
        self.municao=municao
        self.vivo=True
        self.energia=100
    def info(self):
        print("Nome: ", self.nome)
        print("Time: ", self.time)
        print("Força: ", self.forca)
        print("Munição: ", self.municao)
        print("Vivo: ", "sim" if self.vivo else "não")
        print("Energia: ", self.energia)
        print("***********************")
class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca=200
        self.municao=200
        super().__init__(nome, time, self.forca, self.municao)

class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca=100
        self.municao=20
        super().__init__(nome, time, self.forca, self.municao)

    
class Elite(NPC):
    def __init__(self, nome, time):
        self.forca=400
        self.municao=500
        super().__init__(nome, time, self.forca, self.municao)
    def inf(self):
        super().info()

s1=Guarda("Olho Vivo", 1)
s2=Soldado("Bala na agulha",2)
s3=Elite("Ninja", 1)
s4=Guarda("Super Atento", 2)
s5=Soldado("Tiro Certo", 2)
s6=Elite("Fodinha", 2)

s2.info()
s6.inf()
s1.vivo=False
s1.info()




