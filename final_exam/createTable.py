import sqlite3

conn = sqlite3.connect('college.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Students')
cur.execute('CREATE TABLE Students (firstname TEXT, lastName TEXT, id TEXT)')

conn.close()
