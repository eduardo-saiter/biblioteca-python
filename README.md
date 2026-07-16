# 📚 Biblioteca

Sistema de gerenciamento de biblioteca desenvolvido em Python durante meus estudos do curso **Python for Everybody (Py4E)**.

O projeto evoluiu de uma aplicação baseada em JSON para uma arquitetura orientada a objetos utilizando **SQLite** para persistência dos dados.

---

**Status:** 🚧 Em desenvolvimento

---

## 🚀 Funcionalidades

- 📖 Cadastro de livros
- 🔍 Busca por título
- 📚 Listagem do catálogo
- ✏️ Atualização de disponibilidade
- 🗑️ Remoção de livros
- 💾 Persistência em SQLite
- 🧱 Arquitetura em camadas (Model, Repository e Service)

---

## 🏗️ Estrutura do projeto

```
Biblioteca/
│
├── database/
│   ├── database.py
│   └── biblioteca.db
│
├── models/
│   └── livro.py
│
├── repository/
│   └── livro_repository.py
│
├── services/
│   └── biblioteca_services.py
│
├── utils/
│   ├── exibicao.py
│   ├── menu.py
│   └── validacoes.py
│
├── main.py
└── README.md
```

---

## 🛠️ Tecnologias utilizadas

- Python 3
- SQLite3
- Programação Orientada a Objetos (OOP)

---

## ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/eduardo-saiter/biblioteca-python.git
```

Entre na pasta:

```bash
cd biblioteca-python
```

Execute:

```bash
python main.py
```

Na primeira execução, o banco de dados será criado automaticamente caso não exista.

---

## 📌 Arquitetura

O projeto foi dividido em responsabilidades:

- **Model** → representa a entidade `Livro`
- **Repository** → acesso ao banco de dados
- **Service** → regras de negócio
- **Utils** → menus e exibição
- **Database** → conexão e inicialização do SQLite

---

## 📈 Evolução

### ✅ v1.0.0

- Persistência em JSON
- CRUD completo
- Busca de livros
- Empréstimo e devolução

### 🚀 v2.0.0

- Migração completa para SQLite
- Introdução à Programação Orientada a Objetos
- Criação da classe `Livro`
- Separação em camadas (Repository / Service / Model)
- Melhor organização do projeto
- Banco criado automaticamente na inicialização

---

## 🎯 Próximos objetivos (v2.1)

- Melhorar a validação de entradas
- Retornar objetos `Livro` em todas as consultas
- Permitir buscas mais avançadas
- Refatoração de código e redução de duplicação
- Testes automatizados

---

## 📚 Aprendizados

Este projeto faz parte da minha jornada de estudos em Python e acompanha minha evolução durante o curso **Python for Everybody (Py4E)**.

O objetivo é aplicar na prática conceitos como:

- Programação Orientada a Objetos
- SQLite
- Organização de projetos
- Boas práticas de desenvolvimento
- Versionamento com Git e GitHub

---

## 📄 Licença

Projeto desenvolvido para fins de estudo.