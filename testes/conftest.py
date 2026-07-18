import sqlite3

import pytest

from repository.book_repository import BookRepository
from services.library_services import LibraryService


@pytest.fixture
def conn():
    conn = sqlite3.connect(":memory:")

    conn.execute(
        """
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE COLLATE NOCASE,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            available INTEGER NOT NULL DEFAULT 1
        )
        """
    )

    yield conn

    conn.close()


@pytest.fixture
def repository(conn):
    return BookRepository(conn)

@pytest.fixture
def service(repository):
    return LibraryService(repository)
