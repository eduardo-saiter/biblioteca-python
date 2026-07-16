from repository.livro_repository import LivroRepository
from models.livro import Livro
from utils.exibicao import mostrar_dados


class BibliotecaService:

    def __init__(self, repository):
        self.repository = repository

    def adicionar_livro(self):
        titulo = input('Digite o nome do livro: ')
        row = self.repository.existe_titulo(titulo)
        if row is None:
            autor = input('Digite o autor do livro: ')
            try:
                ano = int(input('Digite o ano de publicação do livro: '))
            except ValueError:
                print("Ano inválido. Por favor, insira um número inteiro.")
                return
            livro = Livro(
                None,
                titulo.lower(),
                autor.lower(),
                ano,
                True
            )
            self.repository.inserir(livro)
            print(f"Livro '{titulo}' adicionado com sucesso!")
        else:
            print("Este título já existe, tente novamente")

    def catalogo_biblioteca(self):
        lista = self.repository.listar_biblioteca()
        if lista is not None:
            for livro in lista:
                mostrar_dados(livro)
        else:
            print("Não há nenhum livro na biblioteca")

    def buscar_livro(self):
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

    def emprestar_livro(self):
        busca = input("> ")
        livro = self.repository.buscar_titulo(busca)
        if livro is not None:
            print("Resultado da busca: ")
            mostrar_dados(livro)
            conf = input(f"Quer pegar emprestado o livro {livro.titulo}?")
            if conf.lower() in ("s", "sim"):
                if livro.disponivel:
                    print("Livro esta sendo preparado...")
                    self.repository.atualizar(livro)
                    print("Livro emprestado. Boa Leitura!")
                else:
                    print("Livro indisponível")
            else:
                print("Retornando ao Menu...")
                return

        else:
            print("Nenhum Livro encontrado")
            return

    def devolver_livro(self):
        busca = input("> ")
        livro = self.repository.buscar_titulo(busca)
        if livro is not None:
            print("Resultado da busca: ")
            mostrar_dados(livro)
            conf = input(f"Quer devolver o livro {livro.titulo}? ")
            if conf.lower() in ("s", "sim"):
                if livro.disponivel:
                    print("Livro esta sendo recolhido...")
                    self.repository.atualizar(livro)
                    print(
                        "Livro devolvido. Espero que tenha tido uma excelente leitura.")
                else:
                    print("Este Livro não foi emprestado")
            else:
                print("Retornando ao Menu...")
                return

    def excluir_livro(self):
        titulo = input('Digite o nome do livro: ')
        livro = self.repository.buscar_titulo(titulo)
        if livro is not None:
            id = livro.id
            self.repository.excluir(id)
            print(f"Livro '{titulo}' excluído com sucesso!")
