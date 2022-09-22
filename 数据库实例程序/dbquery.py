import sqlite3

db = sqlite3.connect(r"C:\Users\朱俊杰\Desktop\repo\learn-python\数据库实例程序\test.db")
#其实路径前加r 的作用和\的作用一样，都是为了防止程序将\当作是转义字符，
# 所以r和\在写的时候使用一种方法就可以，当然如果路径是/，那么就不需要涉及这些了！

cur = db.cursor()
sql = "select * from students order by gpa"
cur.execute(sql)
for x in cur.fetchall():
    print(x)
cur.execute("select * from students where age = 18")
print(cur.fetchone())
sql = 'select name,gpa from students where gpa > 3.85 order by birthday desc '
cur.execute(sql)
x = cur.fetchall()
if x != []:
    print("total:",len(x))
    for r in x:
        print(r)
cur.close()
db.close()
