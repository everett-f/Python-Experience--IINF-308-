import sqlite3

conn = sqlite3.connect('college.db')
cur = conn.cursor()


with open("phoneNumbers.txt","r") as customerObj:
    for line in customerObj:
        if line.rstrip() == "": continue
        
        info = line.split();

        if len(info) != 3: continue

        cur.execute("INSERT INTO Students (firstName, lastName, id) VALUES (?, ?, ?)",
            (info[0], info[1], info[2]))


        
conn.commit()
conn.close()
