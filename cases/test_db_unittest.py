# 导包
import unittest
from tools.read_db import ReadDB
# 新建测试类


class TestDB(unittest.TestCase):
    # 定义测试方法
    def test_db(self):
        sql = "select student_id from student where stu_name = '张三'"
        # 调用get_sql_one方法
        data = ReadDB().get_sql_one(sql)
        # 断言
        self.assertEqual(0, data[0])


if __name__ == '__main__':
    unittest.main()