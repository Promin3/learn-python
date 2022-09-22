import sqlite3

db = sqlite3.connect(r"C:\Users\朱俊杰\Desktop\repo\learn-python\数据库实例程序\test.db")
cur = db.cursor()
sql = '''CREATE TABLE if not exists students(id int primary key, name text, gpa real, birthday date, age int, picture blob)'''
cur.execute(sql)
cur.execute("insert into students values (2,'朱凡杰',3.81,'2000-09-12',21,null)")
mylist = [(3, '许云鹏', 3.82, '2003-08-15', 18, None), \
          (4, '于明昊', 3.88, '2002-11-15', 19, None)]
for s in mylist:
    cur.execute("insert into students values (?,?,?,?,?,?)", (s[0], s[1], s[2], s[3], s[4], s[5]))
db.commit()
cur.close()
db.close()