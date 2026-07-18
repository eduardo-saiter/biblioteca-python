from repository.book_repository import BookRepository
from models.book import Book
from utils.exibicao import show_details


class LibraryService:

    def __init__(self, repository: BookRepository) -> None:
        self.repository = repository

    def add_book(self,
                 title: str,
                 author: str,
                 year: str
                 ) -> None:

        if not title:
            raise ValueError("O título não pode ficar vazio")

        if self.repository.title_exists(title):
            raise ValueError("Este título já existe")

        if not author:
            raise ValueError("O autor não pode ficar vazio")

        try:
            year = int(year)
        except ValueError:
            raise ValueError("Ano inválido, insira um valor inteiro")

        book = Book(
            id=None,
            title=title,
            author=author,
            year=year
        )

        self.repository.insert_book(book)

    def catalog_library(self) -> None:
        books = self.repository.list_library()

        if not books:
            print("Nenhum Livro na biblioteca")
            return

        for book in books:
            show_details(book)

    def search_book(self, user_search: str) -> Book | None:
        book = self.repository.title_search(user_search)
        if book is not None:
            print("Resultado da busca: ")
            show_details(book)
            return book
        else:
            print("Nenhum Livro encontrado")
            return

    def lend_book(self, book: Book, conf:str) -> None:
        if book.available:
            if conf.lower() in ("s", "sim"):
                print("Livro esta sendo preparado...")
                self.repository.update_availability(book)
                print("Livro emprestado. Boa Leitura!")
                return
            else:
                print("Retornando ao Menu...")
                return
        else:
            print("Livro Indisponível.")
            return
        
    def return_book(self,book: Book, conf:str) -> None:

        if book.available == False:
            if conf.lower() not in ("s", "sim"):
                print("Retornando ao Menu...")
                return
            else:
                print("Livro está sendo recolhido...")
                self.repository.update_availability(book)
                print("Livro devolvido. Espero que tenha tido uma excelente leitura.")

        else:
            print("Este livro não foi emprestado.")
            return

    def delete_book(self, book: Book, conf:str) -> None:

        if conf.lower() not in ("s", "sim"):
            print("Retornando ao Menu...")
            return
        
        if book.id is None:
            raise ValueError("Não é possível excluir um livro sem ID.")

        self.repository.delete_book(book.id)
        print(f"Livro '{book.title}' excluído com sucesso!")
