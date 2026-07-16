import sqlite3

DB_PATH = "database/biblioteca.db"

def conectar():
    conn = sqlite3.connect(DB_PATH)
    print("Conectado ao Banco!")
    return conn

def inicializar_banco(conn):
    cur = conn.cursor()

    cur.executescript('''
CREATE TABLE IF NOT EXISTS livros(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    titulo TEXT NOT NULL,

    autor TEXT NOT NULL,

    ano INTEGER NOT NULL,

    disponivel INTEGER NOT NULL
);
    ''')
    
    conn.commit()





