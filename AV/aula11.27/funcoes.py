#Funções devem ter prioridade, chame a função depois de sua construção
def media(nota01=0, nota02=0, nota03=0):
    media = round((nota01 + nota02 + nota03) /3)
    return media



nota01 = int(input('Informa a primeira nota: '))
nota02 = int(input('Informa a primeira nota: '))
nota03 = int(input('Informa a primeira nota: '))
media_com_os_tres = media(nota01, nota02, nota03)
media_com_um_vazio = media(nota01, nota02)
print(media_com_os_tres, media_com_um_vazio)


def calcula_horas_extras(quant_hrs, valor_hora):
    horas = float(quant_hrs)
    taxa = float(valor_hora)
    if horas >= 40:
        valor_receber = (horas -40)*taxa
        return valor_receber

quantidade_de_horas = float(input('Informe o total de horas trabalhadas: '))
valor_da_hora = float(input('Informe o valor da taxa do colaborador: ')) 

print(calcula_horas_extras(quantidade_de_horas, valor_da_hora))
