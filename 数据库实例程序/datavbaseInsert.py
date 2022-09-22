import sqlite3

db = sqlite3.connect(r"C:\Users\朱俊杰\Desktop\repo\learn-python\数据库实例程序\test.db")
cur = db.cursor()
stulist = [(1, "朱俊杰", 3.99, '2003-09-01', 18, None), (5, "宋然", 3.80, '2003-08-01', 18, None)]
for s in stulist:
    cur.execute("insert into students values (?,?,?,?,?,?)", (s[0], s[1], s[2], s[3], s[4], s[5]))
db.commit()
cur.close()
db.close()
