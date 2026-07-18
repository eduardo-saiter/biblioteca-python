from services.library_services import LibraryService
from models.book import Book
import pytest


def test_add_book_title_nonexistent(service, repository):
    service.add_book(
        "Python",
        "Charles",
        "2026"
    )

    book = repository.title_search("Python")

    assert book is not None

def test_add_book_title_None(conn, service, repository):

    with pytest.raises(ValueError,match="O título não pode ficar vazio"):
        service.add_book("", "Outro autor", "2026")
    quantity = conn.execute(
        """
        SELECT COUNT(*)
        FROM books
        WHERE title = ?
        """,
        ("Python",)
    ).fetchone()[0]

    assert quantity == 0

def test_add_book_author_None(conn, service, repository):

    with pytest.raises(ValueError,match="O autor não pode ficar vazio"):
        service.add_book("Python", "", "2026")
    quantity = conn.execute(
        """
        SELECT COUNT(*)
        FROM books
        WHERE title = ?
        """,
        ("Python",)
    ).fetchone()[0]

    assert quantity == 0

def test_add_book_year_None(conn, service, repository):

    with pytest.raises(ValueError,match="Ano inválido, insira um valor inteiro"):
        service.add_book("Python", "Charles", "")
    quantity = conn.execute(
        """
        SELECT COUNT(*)
        FROM books
        WHERE title = ?
        """,
        ("Python",)
    ).fetchone()[0]

    assert quantity == 0

def test_catalog_library_empty(capsys,conn, service, repository):

    service.catalog_library()

    captured = capsys.readouterr()

    assert captured.out == "Nenhum Livro na biblioteca\n"

def test_catalog_library(capsys, service, repository):

    service.add_book(
        "Python",
        "Charles",
        "2016"
    )

    service.add_book(
        "Java",
        "James",
        "1992"
    )

    service.catalog_library()

    captured = capsys.readouterr()

    assert "Python" in captured.out
    assert "Charles" in captured.out
    assert "2016" in captured.out
    assert "Java" in captured.out
    assert "James" in captured.out
    assert "1992" in captured.out
  
def test_search_library_book_inexistent(capsys, service, repository):

    user_search = "Python"

    service.search_book(user_search)

    captured = capsys.readouterr()

    assert captured.out == "Nenhum Livro encontrado\n"

def test_search_library_book_existent(capsys, service, repository):

    service.add_book(
        "Python",
        "Charles",
        "2026"
    )

    user_search = "Python"

    service.search_book(user_search)

    captured = capsys.readouterr()

    assert "Python" in captured.out
    assert "Charles" in captured.out
    assert "2026" in captured.out
    
def test_lend_book_available(capsys, service, repository):
    
    service.add_book(
        "Python",
        "Charles",
        "2016"
    )
    user_search = "Python"

    book = service.search_book(user_search)

    service.lend_book(book,"s")

    updated_book = repository.title_search("Python")

    captured = capsys.readouterr()

    assert "Livro emprestado. Boa Leitura!" in captured.out
    assert updated_book.available is False

def test_decline_lend_book_available(capsys, service, repository):
    
    service.add_book(
        "Python",
        "Charles",
        "2016"
    )
    user_search = "Python"

    book = service.search_book(user_search)

    service.lend_book(book,"n")

    updated_book = repository.title_search("Python")

    captured = capsys.readouterr()

    assert "Menu" in captured.out
    assert updated_book.available is True

def test_lend_book_unavailable(capsys, service, repository):
    
    service.add_book(
        "Python",
        "Charles",
        "2016",
    )
    user_search = "Python"

    book = service.search_book(user_search)

    service.lend_book(book,"s")

    book = service.search_book(user_search)

    service.lend_book(book,"s")

    updated_book = repository.title_search("Python")
    
    captured = capsys.readouterr()
    
    assert "Livro Indisponível." in captured.out
    assert updated_book.available is False

def test_return_book_unavailable(capsys, service, repository):
    
    service.add_book(
        "Python",
        "Charles",
        "2016",
    )
    user_search = "Python"

    book = service.search_book(user_search)

    service.lend_book(book,"s")

    book = service.search_book(user_search)
    
    service.return_book(book,"s")

    updated_book = repository.title_search("Python")

    captured = capsys.readouterr()

    assert "Livro devolvido. Espero que tenha tido uma excelente leitura." in captured.out
    assert updated_book.available is True

def test_decline_return_book_available(capsys, service, repository):
    
    service.add_book(
        "Python",
        "Charles",
        "2016"
    )
    user_search = "Python"

    book = service.search_book(user_search)

    service.lend_book(book,"s")

    book = service.search_book(user_search)

    service.return_book(book,"n")

    updated_book = repository.title_search("Python")

    captured = capsys.readouterr()

    assert "Menu" in captured.out
    assert updated_book.available is False

def test_return_book_available(capsys, service, repository):
    
    service.add_book(
        "Python",
        "Charles",
        "2016",
    )

    user_search = "Python"

    book = service.search_book(user_search)

    service.lend_book(book,"s")

    book = service.search_book(user_search)

    service.return_book(book,"s")

    book = service.search_book(user_search)

    service.return_book(book,"s")

    updated_book = repository.title_search("Python")

    captured = capsys.readouterr()

    assert "Este livro não foi emprestado." in captured.out
    assert updated_book.available is True

def test_delete_book_confirmed(capsys, service, repository):
    
    service.add_book(
        "Python",
        "Charles",
        "2016",
    )
    user_search = "Python"

    book = service.search_book(user_search)

    service.delete_book(book,"s")

    updated_book = service.search_book(user_search)

    captured = capsys.readouterr()

    assert "excluído" in captured.out
    assert updated_book is None

def test_delete_book_declined(capsys, service, repository):
    
    service.add_book(
        "Python",
        "Charles",
        "2016",
    )
    user_search = "Python"

    book = service.search_book(user_search)

    service.delete_book(book,"n")

    updated_book = service.search_book(user_search)

    captured = capsys.readouterr()

    assert "Menu" in captured.out
    assert updated_book is not None



