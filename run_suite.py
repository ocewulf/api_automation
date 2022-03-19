# 导包
import unittest
import time
from tools.HTMLTestRunner import HTMLTestRunner
# 组装测试套件
suite = unittest.defaultTestLoader.discover("./cases", pattern="test*.py")
# 指定生成报告的路径及报告文件名
file_path = "./report/{}.html".format(time.strftime("%Y%m%d %H%M%S"))

# 运行测试套件并生成测试报告
with open(file_path, "wb") as f:
    HTMLTestRunner(stream=f).run(suite)