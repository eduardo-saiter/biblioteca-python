from utils.exibicao import (
    mostrar_dados,
)


def adicionar_livro(biblioteca):
    titulo = input('Digite o nome do livro: ')
    for livro in biblioteca:
        if titulo.lower() == livro['titulo']:
            print("Este Livro já existe na biblioteca")
            mostrar_dados(livro, biblioteca)
            return
    autor = input('Digite o autor do livro: ')
    try:
        ano = int(input('Digite o ano de publicação do livro: '))
    except ValueError:
        print("Ano inválido. Por favor, insira um número inteiro.")
        #continue
    livro = {"titulo": titulo.lower(), "autor": autor.lower(), "ano": ano, "disponivel": True}
    biblioteca.append(livro)
    print(f"Livro '{titulo}' adicionado com sucesso!")
    return biblioteca

def listar_livros(biblioteca):
    if not biblioteca:
        print("Nenhum livro cadastrado.")
    for livro in biblioteca:
        mostrar_dados(livro, biblioteca)

def buscar_livros(biblioteca):
    titulo = input("Digite o título do Livro: ")
    print(f"Procurando livro '{titulo}'...")
    encontrado = False
    for livro in biblioteca:
        if titulo.lower() in livro['titulo']:
            mostrar_dados(livro, biblioteca)
            encontrado = True
    
    else:
        print("Livro não encontrado.")
        return None
    

def buscar_livro(biblioteca):
    titulo = input("Digite o título do Livro: ")
    print(f"Procurando livro '{titulo}'...")
    encontrado = False
    for livro in biblioteca:
        if titulo.lower() in livro['titulo']:
            mostrar_dados(livro, biblioteca)
            encontrado = True
            return livro
    else:
        print("Livro não encontrado.")
        return None
      
def emprestar_livro(biblioteca):
    livro = buscar_livro(biblioteca)
    if livro is not None:
        mostrar_dados(livro, biblioteca)
        if livro['disponivel']:
            print("O livro esta disponível")
            print("Anotando empréstimo...")
            livro['disponivel'] = False
            print('Livro emprestado com sucesso.')
        else:
            print("O livro já esta emprestado.")    

    return biblioteca
        


def devolver_livro(biblioteca):
    livro = buscar_livro(biblioteca)
    if livro is not None:
        mostrar_dados(livro, biblioteca)
        if livro['disponivel'] == False:
            print("Anotando devolução...")
            livro['disponivel'] = True
            print('Livro devolvido com sucesso.')
        else:
            print("O livro não foi emprestado.")
    return biblioteca

            
def excluir_livro(biblioteca):
    livro = buscar_livro(biblioteca)
    if livro is not None:
        mostrar_dados(livro, biblioteca)
        titulo = livro['titulo']
        confirmacao = input(f'Deseja confirmar a exclusão do livro {livro['titulo']} (S/N): ')
        if confirmacao.lower() in ('s','sim'):
            print(f'Livro {livro['titulo']} excluído com sucesso!')
            # List Comprehension
            biblioteca = [
            livro # O que entra na lista
            for livro in biblioteca # Percorre a lista
            if livro['titulo'].lower() != titulo.lower() #Filtra a lista
            ]
        elif confirmacao.lower() in ('n', 'nao'):
            print('Livro não excluido, retornando ao Menu')
        else:
            print('Opção Inválida, o livro não será excluído')
        return biblioteca