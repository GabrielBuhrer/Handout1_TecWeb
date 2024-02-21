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
        self.cur = self.conn.execute("SELECT id, title, content FROM note")
        notas = []
        for linha in self.cur:
            id, title, content = linha
            notas.append(Note(id=id, title=title, content=content))
        return  notas

    def update(self,entry):
        self.cur.execute("UPDATE note SET title = ?, content = ? WHERE id = ?", (entry.title,entry.content,entry.id))
        self.conn.commit()
    def delete(self,note_id):
        self.cur.execute("DELETE FROM note WHERE id = ?", (note_id,))
        self.conn.commit()


@dataclass
class Note():
    id: int = None
    title: str = None
    content: str = ''
    