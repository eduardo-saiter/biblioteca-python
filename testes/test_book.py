from models.book import Book


def test_book_create():
    book = Book(
        id=1,
        title="Python para Todos",
        author="Charles Severance",
        year=2016,
        available=True
    )

    assert book.id == 1
    assert book.title == "Python para Todos"
    assert book.author == "Charles Severance"
    assert book.year == 2016
    assert book.available is True


def test_books_with_same_details():
    book1 = Book(
        id=1,
        title="Python",
        author="Charles",
        year=2016,
        available=True
    )

    book2 = Book(
        id=1,
        title="Python",
        author="Charles",
        year=2016,
        available=True
    )

    assert book1 == book2

def test_books_with_diferent_details_true():
    book1 = Book(
        id=1,
        title="PythoJava",
        author="Charles",
        year=2016,
        available=True
    )

    book2 = Book(
        id=1,
        title="Java",
        author="James",
        year=1991,
        available=True
    )

    assert book1 != book2

def test_book_year():
    book = Book(
        id=1,
        title="Python",
        author="Charles",
        year=2016
    )

    assert book.year == 2016

def test_book_tile():
    book = Book(
        id=1,
        title="Python",
        author="Charles",
        year=2016
    )

    assert book.title == "Python"

def test_book_author():
    book = Book(
        id=1,
        title="Python",
        author="Charles",
        year=2016
    )

    assert book.author == "Charles"
