from models.livro import Livro

class LivroRepository():

    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()

    def listar_biblioteca(self):
        self.cur.execute('SELECT * FROM Livros')
        rows = self.cur.fetchall()
        if rows is not None:
            return [Livro(*row) for row in rows]
        else:
            return None
    
    def listar_titulos(self,busca):
        row = self.cur.execute('SELECT * FROM Livros GROUP BY titulo=?',(busca))
        if row is not None:
            return Livro(*row)
        else:
            return None

    def existe_titulo(self, busca):
        self.cur.execute('SELECT * FROM livros WHERE titulo= ?', (busca,))
        return self.cur.fetchone()

    def buscar_titulo(self, busca):
        row = self.existe_titulo(busca)
        if row is None:
            return None
        return Livro(*row)

    def inserir(self, livro):
        self.cur.execute('''
        INSERT INTO livros (titulo, autor, ano, disponivel) VALUES (?,?,?,?)''',
                         (
                             livro.titulo,
                             livro.autor,
                             livro.ano,
                             livro.disponivel
                         ))
        self.conn.commit()

    def atualizar(self,livro):
        id = livro.id
        if livro.disponivel:
            self.cur.execute('''
            UPDATE livros SET disponivel=False WHERE id=?
            ''',(id,))
        else:
            self.cur.execute('''
            UPDATE livros SET disponivel=True WHERE id=?
            ''',(id,))
        self.conn.commit()

    def excluir(self, id):
        self.cur.execute('''
        DELETE FROM livros WHERE id = ?
        ''', (id,))
        self.conn.commit()
