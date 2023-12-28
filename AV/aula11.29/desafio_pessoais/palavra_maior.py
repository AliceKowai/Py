def palavra_mais_longa(texto):
    # Dividir o texto em palavras
    palavras = texto.split()

    # Inicializar a variável para armazenar a palavra mais longa
    palavra_mais_longa = ''

    # Iterar sobre cada palavra no texto
    for palavra in palavras:
        # Verificar se a palavra atual é mais longa do que a armazenada anteriormente
        if len(palavra) > len(palavra_mais_longa):
            palavra_mais_longa = palavra

    return palavra_mais_longa

# Exemplo de uso:
texto_exemplo = "Esta é uma frase de exemplo para encontrar a palavra mais longa"
resultado = palavra_mais_longa(texto_exemplo)
print("A palavra mais longa é:", resultado)
