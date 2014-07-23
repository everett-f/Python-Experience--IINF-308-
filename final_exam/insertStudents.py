import sqlite3

conn = sqlite3.connect('college.db')
cur = conn.cursor()

#cur.execute('DROP TABLE IF EXISTS Students')
#cur.execute('CREATE TABLE Students (firstname TEXT, lastName TEXT, id TEXT)')

cur.execute("INSERT INTO Students (firstName, lastName, id) VALUES (?, ?, ?)",
            ("dong", "Luu", 222999))
cur.execute("INSERT INTO Students (firstName, lastName, id) VALUES (?, ?, ?)",
            ("Everett", "Franco", 5000))
cur.execute("INSERT INTO Students (firstName, lastName, id) VALUES (?, ?, ?)",
            ("Judee", "Oylyer", 3000))
cur.execute("INSERT INTO Students (firstName, lastName, id) VALUES (?, ?, ?)",
            ("nucka", "pumkin", 22239))
cur.execute("INSERT INTO Students (firstName, lastName, id) VALUES (?, ?, ?)",
            ("danny", "playa", 3322434))


conn.commit()

print "Students:"
cur.execute("SELECT * FROM Students")
for row in cur:
    print row


conn.close()
