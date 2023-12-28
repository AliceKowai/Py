def verificar_comun(set01, set02):
    set_comum = set01 & set02 #comum, intersecção
    return set_comum


set01 = {"a", "b", "c", "d", "h", "i", "j", "l", "m"}
set02 = {"a", "e", "i", "o", "u"}
print(verificar_comun(set01, set02))
