class Radio:
    def __init__(self):
        self._ligado = False
        self._volume = 5
        self._frequencia = 101.5

    @property
    def ligado(self):
        return self._ligado

    @ligado.setter
    def ligado(self, valor):
        if isinstance(valor, bool):
            self._ligado = valor
        else:
            raise ValueError("O valor deve ser do tipo booleano (True/False).")

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, valor):
        if 0 <= valor <= 10:
            self._volume = valor
        else:
            raise ValueError("O volume deve estar entre 0 e 10.")

    @property
    def frequencia(self):
        return self._frequencia

    @frequencia.setter
    def frequencia(self, valor):
        if 88.0 <= valor <= 108.0:
            self._frequencia = valor
        else:
            raise ValueError("A frequência deve estar entre 88.0 e 108.0.")

# Teste da classe Radio
meu_radio = Radio()

print(meu_radio.ligado)  # False (valor padrão)
meu_radio.ligado = True
print(meu_radio.ligado)  # True

print(meu_radio.volume)  # 5 (valor padrão)
meu_radio.volume = 7
print(meu_radio.volume)  # 7

print(meu_radio.frequencia)  # 101.5 (valor padrão)
meu_radio.frequencia = 95.7
print(meu_radio.frequencia)  # 95.7
