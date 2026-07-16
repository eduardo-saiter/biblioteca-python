from database.database import (
    inicializar_banco,
    conectar
)

from repository.livro_repository import LivroRepository
from services.biblioteca_services import BibliotecaService
from utils.exibicao import mostrar_menu

conn = conectar()
inicializar_banco(conn)

repositorio = LivroRepository(conn)
service = BibliotecaService(repositorio)

while True:

    mostrar_menu()

    opcao = input("> ")

    if opcao == "1":
        service.adicionar_livro()

    elif opcao == "2":
        service.catalogo_biblioteca()

    elif opcao == "3":
        service.buscar_livro()

    elif opcao == '4':
        service.emprestar_livro()

    elif opcao == '5':
        service.devolver_livro()

    elif opcao == "6":
        service.excluir_livro()

    elif opcao == "7":
        print("Saindo do sistema...")
        conn.close()
        break

    else:
        print("Opção inválida. Tente novamente.")
