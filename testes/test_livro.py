from models.book import Book


def test_criar_livro():
    livro = Book(
        id=1,
        title="Python para Todos",
        author="Charles Severance",
        ano=2016,
        available=True
    )

    assert livro.id == 1
    assert livro.title == "Python para Todos"
    assert livro.author == "Charles Severance"
    assert livro.ano == 2016
    assert livro.available is True


def test_livros_com_mesmos_dados_sao_iguais():
    livro1 = Book(
        id=1,
        title="Python",
        author="Charles",
        ano=2016,
        available=True
    )

    livro2 = Book(
        id=1,
        title="Python",
        author="Charles",
        ano=2016,
        available=True
    )

    assert livro1 == livro2


def test_ano_do_livro():
    livro = Book(
        id=1,
        title="Python",
        author="Charles",
        ano=2016
    )

    assert livro.ano == 2016
