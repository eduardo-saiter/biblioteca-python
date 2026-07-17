from repository.livro_repository import LivroRepository
from models.livro import Livro
from utils.exibicao import mostrar_dados


class BibliotecaService:

    def __init__(self, repository:LivroRepository) -> None:
        self.repository = repository

    def adicionar_livro(self) -> None:
        titulo = input("Digite o nome do livro: ").strip()

        if not titulo:
            print("O título não pode ficar vazio.")
            return

        if self.repository.existe_titulo(titulo):
            print("Este título já existe. Tente novamente.")
            return

        autor = input("Digite o autor do livro: ").strip()

        if not autor:
            print("O autor não pode ficar vazio.")
            return

        try:
            ano = int(input("Digite o ano de publicação do livro: "))
        except ValueError:
            print("Ano inválido. Insira um número inteiro.")
            return

        livro = Livro(
            id = None,
            titulo=titulo,
            autor=autor,
            ano=ano
        )

        self.repository.inserir(livro)
        print(f"Livro '{titulo}' adicionado com sucesso!")

    def catalogo_biblioteca(self) -> None:
        livros = self.repository.listar_biblioteca()

        if not livros:
            print("Não há nenhum livro na biblioteca.")
            return

        for livro in livros:
            mostrar_dados(livro)

    def buscar_livro(self) -> None:
        busca = input("> ")
        livro = self.repository.buscar_titulo(busca)
        if livro is not None:
            print("Resultado da busca: ")
            mostrar_dados(livro)
# livro = self.repository.buscar_autor(busca)
# if livro is not None:
# print("Resultado da busca: ")
# mostrar_dados(livro)
        else:
            print("Nenhum Livro encontrado")
            return

    def emprestar_livro(self) -> None:
        busca = input("> ")
        livro = self.repository.buscar_titulo(busca)
        if livro is not None:
            print("Resultado da busca: ")
            mostrar_dados(livro)
            conf = input(f"Quer pegar emprestado o livro {livro.titulo}?")
            if conf.lower() in ("s", "sim"):
                if livro.disponivel:
                    print("Livro esta sendo preparado...")
                    self.repository.atualizar_disponibilidade(livro)
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

    def devolver_livro(self) -> None:
        busca = input("Título do livro: ")
        livro = self.repository.buscar_titulo(busca)
 
        if livro is None:
            print("Nenhum livro encontrado.")
            return
 
        print("Resultado da busca:")
        mostrar_dados(livro)
 
        conf = input(f"Quer devolver o livro '{livro.titulo}'? ")
    
        if conf.lower() not in ("s", "sim"):
            print("Retornando ao menu...")
            return
    
        if livro.disponivel:
            print("Este livro não foi emprestado.")
            return
    
        print("Livro está sendo recolhido...")
        self.repository.atualizar_disponibilidade(livro)
        print("Livro devolvido. Espero que tenha tido uma excelente leitura.")

    def excluir_livro(self) -> None:
        titulo = input("Digite o nome do livro: ").strip()
        livro = self.repository.buscar_titulo(titulo)

        if livro is None:
            print("Nenhum livro encontrado.")
            return

        if livro.id is None:
            raise ValueError("O livro não possui um ID válido.")
        conf = input(f"Deseja excluir o livro '{livro.titulo}'? ")
    
        if conf.lower() not in ("s", "sim"):
            print("Retornando ao menu...")
            return
        
        livro_id = livro.id
        self.repository.excluir(livro_id)
        print(f"Livro '{livro.titulo}' excluído com sucesso!")
