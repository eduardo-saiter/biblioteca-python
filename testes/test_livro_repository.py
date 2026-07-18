from models.livro import Livro


def test_inserir_livro(conn, repository):

    livro = Livro(
        id=None,
        titulo="Python",
        autor="Charles",
        ano=2016
    )

    repository.inserir(livro)

    row = conn.execute(
        "SELECT titulo, autor, ano FROM livros"
    ).fetchone()

    assert row == ("Python", "Charles", 2016)


def test_buscar_titulo_existente(conn, repository):
    conn.execute(
        """
        INSERT INTO livros (titulo, autor, ano, disponivel)
        VALUES (?, ?, ?, ?)
        """,
        ("Python", "Charles", 2016, True)
    )
    conn.commit()

    livro = repository.buscar_titulo("Python")

    assert livro is not None
    assert livro.titulo == "Python"
    assert livro.autor == "Charles"
    assert livro.ano == 2016


def test_buscar_titulo_inexistente(conn, repository):

    livro = repository.buscar_titulo("Livro inexistente")

    assert livro is None


def test_existe_titulo_retorna_true(conn, repository):
    conn.execute(
        """
        INSERT INTO livros (titulo, autor, ano)
        VALUES (?, ?, ?)
        """,
        ("Python", "Charles", 2016)
    )
    conn.commit()

    resultado = repository.existe_titulo("Python")

    assert resultado is True


def test_existe_titulo_retorna_false(conn, repository):
    resultado = repository.existe_titulo("Java")

    assert resultado is False
