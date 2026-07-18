import sqlite3

import pytest

from repository.book_repository import BookRepository


@pytest.fixture
def conn():
    conn = sqlite3.connect(":memory:")

    conn.execute(
        """
        CREATE TABLE livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL UNIQUE COLLATE NOCASE,
            autor TEXT NOT NULL,
            ano INTEGER NOT NULL,
            disponivel INTEGER NOT NULL DEFAULT 1
        )
        """
    )

    yield conn

    conn.close()


@pytest.fixture
def repository(conn):
    return BookRepository(conn)
