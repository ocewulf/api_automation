from parameterized import parameterized
import unittest


class TestParam(unittest.TestCase):
    @parameterized.expand([("admin", "123456", "abcd"), ("tester", "123456", "adfc")])
    def test_param(self, username, password, code):
        print("用户名:", username)
        print("密码:", password)
        print("验证码:", code)
