# 导包
import pymysql
# 获取连接对象，连接db
conn = pymysql.connect("localhost", "test", "Abcd@1234", "cqxw", charset="utf8")
# 获取游标对象
cur = conn.cursor()
# 执行sql
sql = "select * from student where stu_id = '20010253'"
cur.execute(sql)
# 断言
result = cur.fetchone()
assert 0 == result[0]
# 关闭游标
cur.close()
# 关闭连接
conn.close()
