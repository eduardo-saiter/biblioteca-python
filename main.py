import sqlite3
from database.database import (
    initialize_database,
    connect
)

from repository.book_repository import BookRepository
from services.library_services import LibraryService
from utils.exibicao import show_menu


def main() -> None:
    conn = connect()

    try:

        initialize_database(conn)

        repository = BookRepository(conn)
        service = LibraryService(repository)
        while True:

            show_menu()

            option = input("> ")

            try:

                if option == "1":
                    title = input("> ").strip()
                    author = input("> ").strip()
                    year = input("> ").strip()
                    try:
                        service.add_book(title,author,year)
                        print(f"Livro '{title}' adicionado com sucesso!")
                    except ValueError as e:
                        print(e)

                elif option == "2":
                    service.catalog_library()

                elif option == "3":
                    user_search = input("> ")
                    service.search_book(user_search)

                elif option == '4':
                    user_search = input("> ")
                    book = service.search_book(user_search)
                    if book is not None:
                        conf = input("> ")
                        service.lend_book(book,conf)

                elif option == '5':
                    user_search = input("Título do livro: ")
                    book = service.search_book(user_search)
                    if book is not None:
                        conf = input("> ")
                        service.return_book(book, conf)

                elif option == "6":
                    user_search = input("Digite o nome do livro: ").strip()
                    book = service.search_book(user_search)
                    if book is not None:
                        conf = input("> ")
                        service.delete_book(book, conf)

                elif option == "7":
                    print("Saindo do sistema...")
                    break

                else:
                    print("Opção inválida. Tente novamente.")

            except sqlite3.Error as error:
                print("Erro ao acessar o banco de dados.")
                print(f"Detalhes: {error}")

    except KeyboardInterrupt:
        print("\n Programa interrompido pelo usuário")

    finally:
        conn.close()


if __name__ == '__main__':
    main()
