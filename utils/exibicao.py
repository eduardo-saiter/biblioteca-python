
def mostrar_menu():
    print("===== Biblioteca =====")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Procurar Livro")
    print("4. Emprestar Livro")
    print("5. Devolver Livro")
    print("6. Excluir Livro")
    print("7. Sair")

def mostrar_dados(livro):
    print(f'Título: {livro.titulo.capitalize()}')
    print(f'Autor: {livro.autor.capitalize()}')
    print(f'Ano: {livro.ano}')
    if livro.disponivel:
        print("Disponível : Sim")
    else:
        print('Disponível: Não')