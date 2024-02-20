import sqlite3
from dataclasses import dataclass

class Database():
    def __init__(self, db_name):
       self.db_name = db_name
       self.conn = sqlite3.connect(db_name + ".db")
       self.cur = self.conn.cursor()
       self.cur.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL)")

    def add(self, note):
        self.cur.execute("INSERT INTO note (title, content) VALUES (?, ?)",(note.title, note.content))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        lista = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            n = Note(id=id, title=title, content=content)
            lista.append(n)
        return lista


@dataclass
class Note():
    id: int = None
    title: str = None
    content: str = ''
    