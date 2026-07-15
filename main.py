from services.biblioteca import (
    adicionar_livro,
    excluir_livro,
    emprestar_livro,
    devolver_livro,
    listar_livros,
    buscar_livro,
    buscar_livros,
    

)

from services.persistencia import (
    carregar_biblioteca,
    salvar_biblioteca,
)

from utils.exibicao import (
    mostrar_menu,
    mostrar_dados,
)

biblioteca = carregar_biblioteca()

while True:

    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        biblioteca = adicionar_livro(biblioteca)
        salvar_biblioteca(biblioteca)

    elif opcao == "2":
        listar_livros(biblioteca)
        
    elif opcao == "3":
        livro = buscar_livro(biblioteca)
        mostrar_dados(livro, biblioteca)

    elif opcao == '4':
        biblioteca = emprestar_livro(biblioteca)
        salvar_biblioteca(biblioteca)

    elif opcao == '5':
        biblioteca = devolver_livro(biblioteca)
        salvar_biblioteca(biblioteca)


    elif opcao == "6":
        biblioteca = excluir_livro(biblioteca)
        salvar_biblioteca(biblioteca)
        
    elif opcao == "7":
        print("Saindo do sistema...")
        break
        
    else:
        print("Opção inválida. Tente novamente.")