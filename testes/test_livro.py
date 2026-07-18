from models.livro import Livro

def test_criar_livro():
    livro = Livro(
        id=1,
        titulo="Python para Todos",
        autor="Charles Severance",
        ano=2016,
        disponivel=True
    )

    assert livro.id == 1
    assert livro.titulo == "Python para Todos"
    assert livro.autor == "Charles Severance"
    assert livro.ano == 2016
    assert livro.disponivel is True

def test_livros_com_mesmos_dados_sao_iguais():
    livro1 = Livro(
        id=1,
        titulo="Python",
        autor="Charles",
        ano=2016,
        disponivel=True
    )

    livro2 = Livro(
        id=1,
        titulo="Python",
        autor="Charles",
        ano=2016,
        disponivel=True
    )

    assert livro1 == livro2

def test_ano_do_livro():
    livro = Livro(
        id=1,
        titulo="Python",
        autor="Charles",
        ano=2016
    )

    assert livro.ano == 2016
