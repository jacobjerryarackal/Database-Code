import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                (id INTEGER PRIMARY KEY, name TEXT, position TEXT, salary REAL)''')


employees = [
    (1, 'Alice', 'Manager', 50000.00),
    (2, 'Bob', 'Developer', 60000.00),
    (3, 'Charlie', 'Designer', 45000.00)
]
cursor.executemany('INSERT INTO employees VALUES (?,?,?,?)', employees)


conn.commit()


cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()


for row in rows:
    print(row)


conn.close()