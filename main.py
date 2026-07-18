import sqlite3
from database.database import (
    initialize_database,
    connect
)

from repository.book_repository import BookRepository
from services.libraly_services import LibralyService
from utils.exibicao import show_menu


def main() -> None:
    conn = connect()

    try:

        initialize_database(conn)

        repository = BookRepository(conn)
        service = LibralyService(repository)
        while True:

            show_menu()

            option = input("> ")

            try:

                if option == "1":
                    service.add_book()

                elif option == "2":
                    service.catalog_libraly()

                elif option == "3":
                    service.search_book()

                elif option == '4':
                    service.lend_book()

                elif option == '5':
                    service.return_book()

                elif option == "6":
                    service.delete_book()

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
