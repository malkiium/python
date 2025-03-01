import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS tshirts
            (sky text, name text, size text, price real)''')