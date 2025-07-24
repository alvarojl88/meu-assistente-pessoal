
import sqlite3

def conectar():
    return sqlite3.connect("assistente.db")

def criar_tabelas():
    con = conectar()
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT,
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS despesas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        valor REAL,
        descricao TEXT,
        data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS compras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT,
        comprado BOOLEAN DEFAULT 0,
        data_adicionado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS sono (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dormir TIMESTAMP,
        acordar TIMESTAMP
    )""")

    con.commit()
    con.close()
