from dataclasses import dataclass
@dataclass

class Livro:
        id: int | None
        titulo: str
        autor: str
        ano: int
        disponivel: bool = True
