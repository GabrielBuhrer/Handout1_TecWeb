from database import Database
from database import Note

db = Database('banco')

#--------descomente os códigos abaixo para usar---------

#db.add(Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'))
#db.add(Note(title=None, content='Lembrar de tomar água'))

#notes = db.get_all()
#for note in notes:
#    print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')

#db.update(Note(title='Pão salgado', content='Pão com carne', id=1))

#db.delete(1)
#db.delete(2) 