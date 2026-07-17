import sqlite3
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
DB_PATH = BASE_PATH / "biblioteca.db"


def conectar() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    return conn


def inicializar_banco(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()

    cur.executescript('''
CREATE TABLE IF NOT EXISTS livros(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    titulo TEXT NOT NULL UNIQUE COLLATE NOCASE,

    autor TEXT NOT NULL,

    ano INTEGER NOT NULL,

    disponivel INTEGER NOT NULL DEFAULT 1
);
    ''')

    conn.commit()
