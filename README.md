# 📚 Biblioteca Python

Sistema de gerenciamento de biblioteca executado no terminal, desenvolvido em Python com persistência em SQLite.

O projeto foi criado durante meus estudos de Python e evoluiu de uma aplicação simples para uma arquitetura em camadas, com separação entre modelo, acesso ao banco de dados e regras de negócio.

## Status

**Versão atual:** 2.1.0  
**Situação:** em desenvolvimento

## Funcionalidades

- Cadastrar livros;
- Listar o catálogo completo;
- Buscar livros pelo título;
- Emprestar livros disponíveis;
- Registrar a devolução de livros;
- Excluir livros do catálogo;
- Impedir o cadastro de títulos duplicados;
- Armazenar os dados em um banco SQLite;
- Criar o banco de dados automaticamente na primeira execução;
- Validar título, autor e ano;
- Executar testes automatizados com pytest.

## Tecnologias utilizadas

- Python 3.10 ou superior;
- SQLite;
- `dataclasses`;
- Programação Orientada a Objetos;
- Pytest para testes automatizados.

O programa principal utiliza apenas módulos da biblioteca padrão do Python. O Pytest é necessário somente para desenvolvimento e execução dos testes.

## Estrutura do projeto

```text
Biblioteca/
├── database/
│   ├── database.py
│   └── library.db
├── models/
│   └── book.py
├── repository/
│   ├── __init__.py
│   └── book_repository.py
├── services/
│   ├── __init__.py
│   └── library_services.py
├── testes/
│   ├── conftest.py
│   ├── test_book.py
│   ├── test_book_repository.py
│   └── test_library_services.py
├── utils/
│   ├── __init__.py
│   ├── exibicao.py
│   ├── menu.py
│   └── validacoes.py
├── main.py
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Arquitetura

O projeto está dividido em responsabilidades:

- **Model:** representa a entidade `Book`;
- **Repository:** executa as operações no banco de dados SQLite;
- **Service:** concentra as regras de negócio da biblioteca;
- **Database:** cria e fornece a conexão com o banco;
- **Utils:** contém funções auxiliares de menu, validação e exibição;
- **Main:** controla a interação com o usuário pelo terminal;
- **Testes:** verificam o comportamento dos modelos, repositórios e serviços.

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/eduardo-saiter/biblioteca-python.git
cd biblioteca-python
```

### 2. Criar um ambiente virtual

No Linux ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

A aplicação não possui dependências externas de execução. Para instalar as ferramentas de desenvolvimento:

```bash
python -m pip install -r requirements-dev.txt
```

### 4. Executar o programa

```bash
python main.py
```

Na primeira execução, o arquivo `database/library.db` será criado automaticamente, caso ainda não exista.

## Menu do sistema

O programa permite selecionar operações como:

1. adicionar um livro;
2. listar o catálogo;
3. buscar um livro;
4. emprestar um livro;
5. devolver um livro;
6. excluir um livro;
7. sair do sistema.

## Executando os testes

Com o ambiente virtual ativado e as dependências de desenvolvimento instaladas, execute:

```bash
python -m pytest -q
```

No estado atual do projeto, a suíte possui **33 testes automatizados**.

Para executar um arquivo específico:

```bash
python -m pytest testes/test_library_services.py -v
```

Para executar somente um teste:

```bash
python -m pytest testes/test_library_services.py::nome_do_teste -v
```

## Banco de dados

A aplicação utiliza uma tabela chamada `books`, com os seguintes campos:

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | INTEGER | Identificador único do livro |
| `title` | TEXT | Título único, sem diferenciar maiúsculas de minúsculas |
| `author` | TEXT | Autor do livro |
| `year` | INTEGER | Ano de publicação |
| `available` | INTEGER | Disponibilidade do livro: `1` ou `0` no SQLite |

Ao transformar os registros do banco em objetos `Book`, o Repository converte o campo `available` para `bool`.

## Evolução do projeto

### v1.0.0

- Armazenamento em arquivo JSON;
- Cadastro, busca e exclusão de livros;
- Empréstimo e devolução;
- Estruturas básicas de Python.

### v2.0.0

- Migração para SQLite;
- Introdução à Programação Orientada a Objetos;
- Criação da classe `Book`;
- Separação entre Model, Repository e Service;
- Inicialização automática do banco.

### v2.1.0

- Refatoração do Service para receber dados por parâmetros;
- Separação entre entrada do usuário e regras de negócio;
- Retorno de objetos `Book` nas buscas;
- Conversão de valores do SQLite para booleanos;
- Validações aprimoradas;
- Testes automatizados com Pytest.

## Próximos objetivos

- Criar buscas parciais por título e autor;
- Melhorar as mensagens e a interface do terminal;
- Adicionar registro de usuários;
- Registrar histórico de empréstimos;
- Adicionar datas de empréstimo e devolução;
- Ampliar a cobertura de testes;
- Criar uma interface gráfica ou API.

## Aprendizados

Este projeto aplica conceitos como:

- classes e objetos;
- `dataclasses`;
- type hints;
- tratamento de exceções;
- SQLite e comandos SQL;
- arquitetura em camadas;
- separação de responsabilidades;
- injeção de dependência;
- testes com fixtures e `capsys`;
- Git e GitHub.

## Licença

Projeto desenvolvido para fins de estudo.
