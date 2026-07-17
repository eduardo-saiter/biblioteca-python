import sqlite3
from models.livro import Livro

class LivroRepository:

    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn
        self.cur = conn.cursor()

    def listar_biblioteca(self) -> list[Livro]:
        self.cur.execute('SELECT * FROM Livros')
        rows = self.cur.fetchall()
        return [Livro(*row) for row in rows]

    def existe_titulo(self, busca: str) -> bool:
        self.cur.execute('SELECT * FROM livros WHERE titulo= ?', (busca.strip().lower(),))
        return self.cur.fetchone() is not None

    def buscar_titulo(self, busca: str) -> Livro | None:
        self.cur.execute(
            '''
            SELECT id, titulo, autor, ano, disponivel
            FROM livros
            WHERE titulo = ?
            ''',
            (busca.strip().lower(),)
        )
        row = self.cur.fetchone()
        if row is None:
            return None
        return Livro(*row)

    def inserir(self, livro: Livro) -> None:
        self.cur.execute('''
        INSERT INTO livros (titulo, autor, ano, disponivel) VALUES (?,?,?,?)''',
                         (
                             livro.titulo,
                             livro.autor,
                             livro.ano,
                             livro.disponivel
                         ))
        self.conn.commit()

    def atualizar_disponibilidade(self,livro: Livro) -> None:
        if livro.id is None:
            raise ValueError("Não é possível atualizar um livro sem ID.")
        novo_status = not livro.disponivel

        self.cur.execute(
            """
            UPDATE livros
            SET disponivel = ?
            WHERE id = ?
            """,
            (novo_status, livro.id)
        )

        self.conn.commit()

    def excluir(self, livro_id:int ) -> None:
        self.cur.execute('''
        DELETE FROM livros WHERE id = ?
        ''', (livro_id,)
        )
        self.conn.commit()
