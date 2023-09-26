import os
import random

def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

jogar_novamente = "s"

def iniciar_jogo():
    global jogar_novamente
    jogar_novamente = "s"  # Definir como "s" inicialmente para começar o jogo

    while jogar_novamente == "s":
        jogadas = 0
        quem_joga = 2
        max_jogadas = 9
        vit = "n"
        velha = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        def tela():
            limpar_tela()
            print("  0   1   2")
            print("0:  ", velha[0][0], " | ", velha[0][1], " | ", velha[0][2])
            print(" -------------------")
            print("1:  ", velha[1][0], " | ", velha[1][1], " | ", velha[1][2])
            print(" -------------------")
            print("2:  ", velha[2][0], " | ", velha[2][1], " | ", velha[2][2])
            print("jogadas: ", jogadas)

        def jogador_joga():
            nonlocal jogadas
            nonlocal quem_joga
            nonlocal max_jogadas
            if quem_joga == 2 and jogadas < max_jogadas:
                try:
                    l = int(input("Linha: "))
                    c = int(input("Coluna: "))
                    while l < 0 or l > 2 or c < 0 or c > 2 or velha[l][c] != " ":
                        print("Jogada inválida. Tente novamente.")
                        l = int(input("Linha: "))
                        c = int(input("Coluna: "))
                    velha[l][c] = "X"
                    quem_joga = 1
                    jogadas += 1
                except:
                    print("Linha e/ou coluna inválida")
                    os.system("pause")

        def cpu_joga():
            nonlocal jogadas
            nonlocal quem_joga
            nonlocal max_jogadas
            if quem_joga == 1 and jogadas < max_jogadas:
                l = random.randrange(0, 3)
                c = random.randrange(0, 3)
                while velha[l][c] == "X" or velha[l][c] == "O":
                    l = random.randrange(0, 3)
                    c = random.randrange(0, 3)
                velha[l][c] = "O"
                jogadas += 1
                quem_joga = 2

        def verificar_vitoria():
            nonlocal velha
            vitoria = "n"
            simbolo = ["X", "O"]
            for s in simbolo:
                # Verificar linhas
                for il in range(3):
                    soma = 0
                    for ic in range(3):
                        if velha[il][ic] == s:
                            soma += 1
                    if soma == 3:
                        vitoria = s
                        break

                # Verificar colunas
                for ic in range(3):
                    soma = 0
                    for il in range(3):
                        if velha[il][ic] == s:
                            soma += 1
                    if soma == 3:
                        vitoria = s
                        break

                # Verificar diagonal 1
                soma = 0
                for i in range(3):
                    if velha[i][i] == s:
                        soma += 1
                if soma == 3:
                    vitoria = s

                # Verificar diagonal 2
                soma = 0
                for i in range(3):
                    if velha[i][2 - i] == s:
                        soma += 1
                if soma == 3:
                    vitoria = s

                if vitoria != "n":
                    break

            return vitoria

        def verificar_empate():
            nonlocal velha
            for i in range(3):
                for j in range(3):
                    if velha[i][j] == " ":
                        return False
            return True

        while True:
            tela()
            jogador_joga()
            tela()
            vit = verificar_vitoria()
            if vit != "n" or jogadas >= max_jogadas:
                break

            cpu_joga()
            tela()
            vit = verificar_vitoria()
            if vit != "n" or jogadas >= max_jogadas:
                break

        print("fim de jogo")
        if vit == "X" or vit == "O":
            print("jogador", vit, "venceu")
        else:
            if verificar_empate():
                print("EMPATE!")
            else:
                print("Ocorreu um erro no código.")  
        jogar_novamente = input("Jogar novamente? [s/n]: ").lower()

    print("Obrigado por jogar! Até a próxima!")

iniciar_jogo()
