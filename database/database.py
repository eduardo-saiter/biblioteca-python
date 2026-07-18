import sqlite3
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
DB_PATH = BASE_PATH / "library.db"


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    return conn


def initialize_database(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()

    cur.executescript('''
CREATE TABLE IF NOT EXISTS books(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL UNIQUE COLLATE NOCASE,

    author TEXT NOT NULL,

    year INTEGER NOT NULL,

    available INTEGER NOT NULL DEFAULT 1
);
    ''')

    conn.commit()
