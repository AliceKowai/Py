class FoneDeOuvido:
    def get_volume(self):
        return self.__volume
    def set_volume(self, novo_volume):
        self.__volume = novo_volume

    volume = property(get_volume, set_volume)
#No propety, chamada do atributo direto nos set e get, deve ser privado, ou seja __

fone = FoneDeOuvido()
fone.volume = 200 #um jeito de fazer o set
print(fone.volume) #um jeito de fazer o get
fone.set_volume(30)
print(fone.get_volume())
fone.set_volume(20)
print(fone.volume)

