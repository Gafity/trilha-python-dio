import sqlite3
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent

conexao = sqlite3.connect(ROOT_FOLDER / "meu_banco.db")
CURSOR = conexao.cursor()
CURSOR.row_factory = sqlite3.Row


def criar_tabelas(conexao, cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100), email VARCHAR(150);
    )"""
    )


def inserir_registros(conexao, cursor, data):
    # É sempre bom quando for inserir registros em uma tabela usar query preparadas com (?,?)
    data = ("Giovana", "gi@email.br")
    cursor.execute("INSERT INTO clientes(nome, email) VALUES (?,?);", data)
    conexao.commit()

    # Maneira errada | CURSOR.execute(f"INSERT INTO clientes(nome, email) VALUES ({nome}, {email});")
    # Como as variaveis estão sendo concatenadas por f-string eu poderia passar um comando 1=1
    # E logo em seguida um DROPE TABLE ou recuperar todos os valores da tabela etc


def atualizar_registros(conexao, cursor, data):
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()


# A operação delete é usada para remover registros
def excluir_registros(conexao, cursor, Id):
    # Quando for passar um tupla com um unico valor, usem "," (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", Id)
    conexao.commit()


def inserir_muitos(conexao, cursor, data):
    cursor.executemany("INSERT INTO clientes(nome, email) VALUES(?, ?);", data)
    conexao.commit()


def recuperar_cliente(cursor, Id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (Id,))
    return cursor.fetchone()


def recuperar_clientes(cursor):
    cursor.execute("SELECT * FROM clientes ORDER BY nome")
    return cursor.fetchall()
