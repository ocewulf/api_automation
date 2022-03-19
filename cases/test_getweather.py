# 导包
import unittest
from api.api_getweather import ApiWeather
from parameterized import parameterized
from tools.read_file import ReadFile


# 读取参数文件，获取指定格式的参数并传参
def get_data():
    datas = ReadFile("param.json").read_file()
    # print(data)
    # 新建空列表
    arr = []
    for data in datas.values():
        arr.append((data.get("url"),
                          data.get("apiKey"),
                          data.get("area"),
                          data.get("areaID"),
                          data.get("expected"),
                          data.get("status_code")
                          ))
    return arr


# 定义测试类继承unnitest.TestCase
class TestGetWeather(unittest.TestCase):
    # 定义获取天气的测试方法
    @parameterized.expand(get_data())
    def test_get_weather(self, url, apiKey, area, areaID, expected, status_code):
        # 定义测试数据url、apiKey、area、areaID
        # url = "http://api.apishop.net/common/weather/get15DaysWeatherByArea"
        # apiKey = "7AGvisd25c65a0f67a96a1da5955f8bf9a8db3157d119f8"
        # area = "长沙"
        # areaID = "101250101"
        # 调用api.getweather方法并返回天气信息
        res = ApiWeather().get_weather(url, apiKey, area, areaID)
        print(res.text)
        print(res.status_code)
        # r = json.dumps(res.text)
        # print(r)
        # print(type(r))
        # 断言响应码和响应信息
        self.assertEqual(status_code, res.status_code)
        self.assertIn(expected, res.text, msg=None)


if __name__ == '__main__':
    unittest.main()
