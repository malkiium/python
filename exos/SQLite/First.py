import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS tshirts
            (sky text PRIMARY KEY, name text, size text, price real)''')


cur.execute('''INSERT OR IGNORE INTO tshirts VALUES
            ('SKU1234', 'Black Logo Tshirt', 'M', 19.99)''')

cur.execute('''INSERT OR IGNORE INTO tshirts VALUES
            ('SKU1235', 'Black Logo Tshirt', 'L', 19.99)''')


con.commit()

for row in cur.execute('SELECT * FROM tshirts'):
    print(row)