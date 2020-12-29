# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('email.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')
cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox-short.txt'

fhand = open(fname)

for line in fhand:
    if line.startswith('From: '):
        pieces = line.split()
        email = pieces[1]
        cur.execute('SELECT count FROM Counts WHERE email=? ', (email, ))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (email, count) VALUES (?, 1)''', (email, ))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email, ))
    conn.commit()


sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()