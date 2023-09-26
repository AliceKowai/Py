import os
import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    caminho="C:\\Users\\alice\\Documents\\Py\\IntensivaoPy\\bd\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
vcon= ConexaoBanco()

def menu_inserir():
    print("")

def menu_deletar():
    print("")

def menu_atualizar():
    print("")

def menu_consultar():
    print("")

def menu_consultar_nomes():
    print("")


def menuPrincipal():
    os.system("cls")
    print("1 - Inserir um Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registro por ID")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")

    opc=0
    while opc !=6:
        menuPrincipal()
        opc=int(input("Digite uma opção"))
        if opc==1:
            menu_inserir()
        elif opc==2:
            menu_deletar()
        elif opc==3:
            menu_atualizar()
        elif opc==4:
            menu_consultar()
        elif opc==5:
            menu_consultar_nomes()
        elif opc==6:
            os.system("cls")
            print("Programa finalizado")
        else:
            os.system("cls")
            print("Opção Inválida")
    os.system("pause")