import sqlite3
from sqlite3 import Error

#### Criar conexão ###
def ConexaoBanco():
    caminho="C:\\Users\\alice\\Documents\\Py\\IntensivaoPy\\bd\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

##### Criar Tabela

vsql="""CREATE TABLE tb_contatos(
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR(30),
            T_TELEFONECONTATO VARCHAR(14),
            T_EMAILCONTATO VARCHAR(30)
        );"""

def criar_tabela(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada")
    except Error as ex:
        print(ex)


#nome=input("Digite o nome: ")
#telefone=input("Digite o telefone: ")
#email=input("Digite o email: ")



#vsql="INSERT INTO tb_contatos(T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)VALUES('"+nome+"', '"+telefone+"', '"+email+"')"

## inserir ##
def inserir(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro inserido")
    except Error as ex:
        print(ex)

## deletar ##
def deletar(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro inserido")
    except Error as ex:
        print(ex)
    finally:
        print("Registro removido")

## update ##
def atualizar(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro atualizado")

## consulta ##
def consulta(conexao, sql):
    c=conexao.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    return resultado

#vsql="SELECT * FROM tb_contatos"
#vsql="SELECT * FROM tb_contatos WHERE T_NOMECONTATO='Ali'"
vsql="SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE'A%'"

#vsql="UPDATE tb_contatos SET T_NOMECONTATO='Floki', T_TELEFONECONTATO='(88)918182838', T_EMAILCONTATO='floki@email.com' WHERE N_IDCONTATO=2"
#vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO=6"

#deletar(vcon, vsql)
#criar_tabela(vcon,vsql)
#inserir(vcon,vsql)
#atualizar(vcon, vsql)
res=consulta(vcon, vsql)
for r in res:
    print(r)
    print(type(r))
vcon.close()
