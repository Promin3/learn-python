import sqlite3

db = sqlite3.connect("test.db")
cur = db.cursor()
sql = "update students set gpa = ? where name =?"
cur.execute(sql, (4.0, '朱俊杰'))
db.commit()
cur.close()
db.close()
