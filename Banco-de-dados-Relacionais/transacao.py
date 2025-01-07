import sqlite3
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent

conexao = sqlite3.connect(ROOT_FOLDER / "meu_banco.db")
CURSOR = conexao.cursor()
CURSOR.row_factory = sqlite3.Row

try:
    CURSOR.execute("INSERT INTO clientes (nome, email) VALUES(?, ?)", ("teste1", "teste1@email.com"))
    CURSOR.execute("INSERT INTO clientes (id, nome, email) VALUES(?, ?, ?)", (1, "teste2", "teste@email.com"))
    conexao.commit()
except Exception as ex:
    print(f"Ops! Um error ocorreu: {ex}")
    conexao.rollback()