from models.book import Book
import sqlite3
import pytest


def test_insert_book(conn, repository):

    book = Book(
        id=None,
        title="Python",
        author="Charles",
        year=2016
    )

    repository.insert_book(book)

    row = conn.execute(
        "SELECT title, author, year FROM books"
    ).fetchone()

    assert row == ("Python", "Charles", 2016)

def test_insert_book_same_title(conn, repository):

    book1 = Book(
        id=None,
        title="Python",
        author="Charles",
        year=2016
    )

    book2 = Book(
        id=None,
        title="Python",
        author="Charles",
        year=2016
    )

    repository.insert_book(book1)

    with pytest.raises(sqlite3.IntegrityError):
        repository.insert_book(book2)

def test_search_existent_title(conn, repository):
    conn.execute(
        """
        INSERT INTO books (title, author, year, available)
        VALUES (?, ?, ?, ?)
        """,
        ("Python", "Charles", 2016, True)
    )
    conn.commit()

    book = repository.title_search("Python")

    assert book is not None
    assert book.title == "Python"
    assert book.author == "Charles"
    assert book.year == 2016

def test_search_nonexistent_title(conn, repository):

    book = repository.title_search("Livro inexistente")

    assert book is None

def test_title_exist_return_true(conn, repository):
    conn.execute(
        """
        INSERT INTO books (title, author, year)
        VALUES (?, ?, ?)
        """,
        ("Python", "Charles", 2016)
    )
    conn.commit()

    result = repository.title_exists("Python")

    assert result is True

def test_title_exist_return_false(conn, repository):
    result = repository.title_exists("Java")

    assert result is False

def test_list_library(conn,repository):

    conn.execute(
        """
        INSERT INTO books (title, author, year, available)
        VALUES (?, ?, ?, ?)
        """,
        ("Python", "Charles", 2016, True)
    )
    conn.commit()

    books = repository.list_library()

    assert books == [Book(id=1, title= "Python", author="Charles", year=2016, available=True)]

def test_list_empty_library(conn,repository):

    books = repository.list_library()

    assert books == []

def test_update_availability_book_available(conn, repository):
    conn.execute(
        """
        INSERT INTO books (title, author, year, available)
        VALUES (?, ?, ?, ?)
        """,
        ("Python", "Charles", 2016, True)
    )
    conn.commit()

    row = conn.execute(
        """
        SELECT id, title, author, year, available
        FROM books
        WHERE title = ?
        """,
        ("Python",)
    ).fetchone()

    book = Book(*row)

    repository.update_availability(book)

    result = conn.execute(
        """
        SELECT available
        FROM books
        WHERE title = ?
        """,
        ("Python",)
    ).fetchone()

    assert result == (0,)

def test_update_availability_book_noneavailably(conn, repository):

    conn.execute(
        """
        INSERT INTO books (title, author, year, available)
        VALUES (?, ?, ?, ?)
        """,
        ("Python", "Charles", 2016, False)
    )
    conn.commit()

    row = conn.execute(
        """
        SELECT id, title, author, year, available
        FROM books
        WHERE title = ?
        """,
        ("Python",)
    ).fetchone()

    book = Book(*row)

    repository.update_availability(book)

    result = conn.execute(
        """
        SELECT available
        FROM books
        WHERE title = ?
        """,
        ("Python",)
    ).fetchone()

    assert result == (1,)

def test_delete_book_existent(conn, repository):

    conn.execute("""
    INSERT INTO books (title, author, year, available)
    VALUES (?,?,?,?)
    """,
    ("Python","Charles",2016,True)
    )

    conn.commit()

    row = conn.execute(
        """
        SELECT id, title, author, year, available
        FROM books
        WHERE title = ?
        """,
        ("Python",)
    ).fetchone()

    book = Book(*row)

    repository.delete_book(book.id)

    result = conn.execute("SELECT id FROM books WHERE title=?",("Python",)).fetchone()

    assert result == None








        