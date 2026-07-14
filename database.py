import sqlite3

def create_database():

    conn=sqlite3.connect("students.db")

    cur=conn.cursor()

    cur.execute("""

CREATE TABLE IF NOT EXISTS students(

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT,

age INTEGER,

attendance REAL,

marks REAL,

income REAL,

dropout INTEGER

)

""")

    conn.commit()

    conn.close()
