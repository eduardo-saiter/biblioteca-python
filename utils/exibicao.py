from models.book import Book


def show_menu() -> None:
    print("===== Biblioteca =====")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Procurar Livro")
    print("4. Emprestar Livro")
    print("5. Devolver Livro")
    print("6. Excluir Livro")
    print("7. Sair")


def show_details(livro: Book) -> None:
    print(f'Título: {livro.title}')
    print(f'Autor: {livro.author}')
    print(f'Ano: {livro.year}')
    if livro.available:
        print("Disponível : Sim")
    else:
        print('Disponível: Não')
