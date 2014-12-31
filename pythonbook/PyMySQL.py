# -*- coding: utf-8 -*-
# file: PyMySQL.py
#
import MySQLdb
db = MySQLdb.connect(host='localhost',
					user='root',
					passwd='apec@52827',
					db='python')
cur = db.cursor()
cur.execute('INSERT INTO people (name, age, sex) VALUES (\'Jee\',21,\'F\')')
r = cur.execute('DELETE FROM people where age=20')
db.commit()
r = cur.execute('SELECT * FROM people')
r = cur.fetchall()
print r
cur.close()
db.close()