import _sqlite3

connection = _sqlite3.connect('Mtuci_db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS student_group (
numb VARCHAR NOT NULL,
chair varchar NOT NULL
)
''')

cursor.execute('''INSERT INTO student_group (numb, chair) VALUES ('БВТ2001', 'МКиИТ')''')

cursor.execute('''SELECT chair FROM student_group WHERE numb="БВТ2001"''')
chairs = cursor.fetchall()

for chair in chairs:
    print(chair)

cursor.execute('''DELETE FROM student_group WHERE numb="БВТ2001"''')

cursor.execute('''UPDATE student_group SET numb='БИН2005' WHERE chair="СиСС"''')

cursor.execute('''CREATE TABLE student(
id SERIAL PRIMARY KEY,
full_name varchar NOT NULL,
passport varchar(10) NOT NULL,
group_numb varchar REFERENCES
student_group(numb)
)
''')

connection.commit()
connection.close()