# 📚 Sistema de Controle de Biblioteca

**Status:** 🚧 Em desenvolvimento

Um sistema de gerenciamento de biblioteca desenvolvido em Python durante meus estudos com o curso **Python for Everybody (Py4E)**.

O projeto é executado pelo terminal e permite cadastrar, consultar e gerenciar empréstimos de livros, utilizando arquivos JSON para persistência dos dados.

---

## ✨ Funcionalidades

- Adicionar livros
- Listar todos os livros
- Buscar livros por título
- Emprestar livros
- Devolver livros
- Excluir livros
- Armazenamento permanente em arquivo JSON

---

## 📁 Estrutura do Projeto

```text
Biblioteca/
│
├── main.py
├── biblioteca.json
├── README.md
│
├── services/
│   ├── biblioteca.py
│   ├── persistencia.py
│   └── __init__.py
│
└── utils/
    ├── exibicao.py
    └── __init__.py
```

### main.py

Responsável pelo menu principal e pelo fluxo da aplicação.

### services/

Contém toda a lógica do sistema.

- **biblioteca.py** → operações sobre os livros
- **persistencia.py** → leitura e escrita do arquivo JSON

### utils/

Funções auxiliares para exibição das informações no terminal.

### biblioteca.json

Arquivo responsável por armazenar todos os livros cadastrados.

---

## 💻 Tecnologias utilizadas

- Python 3
- JSON
- Programação estruturada
- Manipulação de arquivos

---

## 🚀 Como executar

Clone o repositório:

```bash
git clone <url-do-repositorio>
```

Entre na pasta:

```bash
cd Biblioteca
```

Execute:

```bash
python main.py
```

---

## 📖 O que aprendi neste projeto

Durante o desenvolvimento deste sistema pratiquei:

- Estruturas de repetição
- Condicionais
- Listas
- Dicionários
- Tuplas
- Funções
- Organização de projetos
- Módulos
- Persistência de dados com JSON
- Tratamento de exceções (`try/except`)
- List Comprehension

---

## 🔨 Melhorias futuras

- [ ] Pesquisa por autor
- [ ] Edição de livros
- [ ] Identificador único (ID) para cada livro
- [ ] Banco de dados SQLite
- [ ] Interface gráfica ou Web
- [ ] API utilizando FastAPI
- [ ] Integração com um agente de IA

---

## 🎯 Objetivo

Este projeto foi desenvolvido para praticar conceitos fundamentais de Python, incluindo estruturas de dados, funções, manipulação de arquivos, módulos e organização de projetos.

O objetivo é evoluí-lo gradualmente conforme avanço nos estudos, incorporando conceitos como Programação Orientada a Objetos, banco de dados, APIs REST e agentes de Inteligência Artificial.