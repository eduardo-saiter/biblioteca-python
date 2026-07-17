from models.livro import Livro

def mostrar_menu() -> None:
    print("===== Biblioteca =====")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Procurar Livro")
    print("4. Emprestar Livro")
    print("5. Devolver Livro")
    print("6. Excluir Livro")
    print("7. Sair")

def mostrar_dados(livro: Livro) -> None:
    print(f'Título: {livro.titulo}')
    print(f'Autor: {livro.autor}')
    print(f'Ano: {livro.ano}')
    if livro.disponivel:
        print("Disponível : Sim")
    else:
        print('Disponível: Não')