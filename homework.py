import _sqlite3

connection = _sqlite3.connect('Homework_db')
connection.execute("PRAGMA foreign_keys = 1")

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Departament (
title_caf TEXT PRIMARY KEY,
dean TEXT NOT NULL
)
''')

masDep = [('СИСС', 'СИСС'), ('РИИТ', 'РИИТ')]

cursor.executemany('''INSERT INTO Departament (title_caf, dean) VALUES (?, ?)''', masDep)

cursor.execute('''
CREATE TABLE IF NOT EXISTS Student_group (
title_group TEXT PRIMARY KEY,
title_caf TEXT NOT NULL,
FOREIGN KEY(title_caf) REFERENCES Departament(title_caf)
)
''')

masStGr = [('БИН2301', 'СИСС'), ('БИН2005', 'СИСС'), ('РИИТ2001', 'РИИТ'), ('РИИТ2302', 'РИИТ')]
cursor.executemany('''INSERT INTO Student_group (title_group, title_caf) VALUES (?, ?)''', masStGr)

cursor.execute('''
CREATE TABLE IF NOT EXISTS Student (
id SERIAL PRIMARY KEY,
name TEXT NOT NULL,
passport VARCHAR NOT NULL,
title_group TEXT NOT NULL,
FOREIGN KEY(title_group) REFERENCES Student_group(title_group)
)
''')

masSt = [('Jax', 23465, 'БИН2301'),
         ('Keks', 23575, 'БИН2301'),
         ('Meel', 32523, 'РИИТ2001'),
         ('Meat', 32355, 'РИИТ2302'),
         ('Lox', 23525, 'БИН2005')]

cursor.executemany('''INSERT INTO Student (name, passport, title_group) VALUES (?, ?, ?)''', masSt)

connection.commit()
connection.close()