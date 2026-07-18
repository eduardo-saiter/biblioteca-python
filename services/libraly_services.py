from repository.book_repository import BookRepository
from models.book import Book
from utils.exibicao import show_details


class LibralyService:

    def __init__(self, repository: BookRepository) -> None:
        self.repository = repository

    def add_book(self) -> None:
        title = input("Digite o nome do livro: ").strip()

        if not title:
            print("O título não pode ficar vazio.")
            return

        if self.repository.title_exists(title):
            print("Este título já existe. Tente novamente.")
            return

        author = input("Digite o autor do livro: ").strip()

        if not author:
            print("O autor não pode ficar vazio.")
            return

        try:
            year = int(input("Digite o ano de publicação do livro: "))
        except ValueError:
            print("Ano inválido. Insira um número inteiro.")
            return

        book = Book(
            id=None,
            title=title,
            author=author,
            year=year
        )

        self.repository.insert_book(book)
        print(f"Livro '{title}' adicionado com sucesso!")

    def catalog_libraly(self) -> None:
        books = self.repository.list_libraly()

        if not books:
            print("Não há nenhum livro na biblioteca.")
            return

        for book in books:
            show_details(book)

    def search_book(self) -> None:
        user_search = input("> ")
        book = self.repository.title_search(user_search)
        if book is not None:
            print("Resultado da busca: ")
            show_details(book)
# livro = self.repository.buscar_autor(busca)
# if livro is not None:
# print("Resultado da busca: ")
# mostrar_dados(livro)
        else:
            print("Nenhum Livro encontrado")
            return

    def lend_book(self) -> None:
        user_search = input("> ")
        book = self.repository.title_search(user_search)
        if book is not None:
            print("Resultado da busca: ")
            show_details(book)
            conf = input(f"Quer pegar emprestado o livro {book.title}?")
            if conf.lower() in ("s", "sim"):
                if book.available:
                    print("Livro esta sendo preparado...")
                    self.repository.update_availability(book)
                    print("Livro emprestado. Boa Leitura!")
                    return
                else:
                    print("Livro indisponível.")
                    return
            else:
                print("Retornando ao Menu...")
                return
        else:
            print("Nenhum Livro encontrado")
            return

    def return_book(self) -> None:
        user_search = input("Título do livro: ")
        book = self.repository.title_search(user_search)

        if book is None:
            print("Nenhum livro encontrado.")
            return

        print("Resultado da busca:")
        show_details(book)

        conf = input(f"Quer devolver o livro '{book.title}'? ")

        if conf.lower() not in ("s", "sim"):
            print("Retornando ao menu...")
            return

        if book.available:
            print("Este livro não foi emprestado.")
            return

        print("Livro está sendo recolhido...")
        self.repository.update_availability(book)
        print("Livro devolvido. Espero que tenha tido uma excelente leitura.")

    def delete_book(self) -> None:
        title = input("Digite o nome do livro: ").strip()
        book = self.repository.title_search(title)

        if book is None:
            print("Nenhum livro encontrado.")
            return

        if book.id is None:
            raise ValueError("O livro não possui um ID válido.")
        conf = input(f"Deseja excluir o livro '{book.title}'? ")

        if conf.lower() not in ("s", "sim"):
            print("Retornando ao menu...")
            return

        book_id = book.id
        self.repository.delete_book(book_id)
        print(f"Livro '{book.title}' excluído com sucesso!")
