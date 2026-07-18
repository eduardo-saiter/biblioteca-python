import sqlite3
from models.book import Book


class BookRepository:

    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn
        self.cur = conn.cursor()

    def list_libraly(self) -> list[Book]:
        self.cur.execute('SELECT * FROM books')
        rows = self.cur.fetchall()
        return [Book(*row) for row in rows]

    def title_exists(self, user_search: str) -> bool:
        self.cur.execute('SELECT * FROM books WHERE title= ?',
                         (user_search.strip().lower(),))
        return self.cur.fetchone() is not None

    def title_search(self, user_search: str) -> Book | None:
        self.cur.execute(
            '''
            SELECT id, title, author, year, available
            FROM books
            WHERE title = ?
            ''',
            (user_search.strip().lower(),)
        )
        row = self.cur.fetchone()
        if row is None:
            return None
        return Book(*row)

    def insert_book(self, book: Book) -> None:
        self.cur.execute('''
        INSERT INTO books (title, author, year, available) VALUES (?,?,?,?)''',
                         (
                             book.title,
                             book.author,
                             book.year,
                             book.available
                         ))
        self.conn.commit()

    def update_availability(self, book: Book) -> None:
        if book.id is None:
            raise ValueError("Não é possível atualizar um livro sem ID.")
        new_status = not book.available

        self.cur.execute(
            """
            UPDATE books
            SET available = ?
            WHERE id = ?
            """,
            (new_status, book.id)
        )

        self.conn.commit()

    def delete_book(self, book_id: int) -> None:
        self.cur.execute('''
        DELETE FROM books WHERE id = ?
        ''', (book_id,)
        )
        self.conn.commit()
