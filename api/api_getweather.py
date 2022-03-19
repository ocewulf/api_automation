import json

import requests
from requests_toolbelt.multipart import MultipartEncoder


# 新建获取天气对象
class ApiWeather(object):
    # 新建获取天气方法
    def get_weather(self, url, apiKey, area, areaID):
        # 定义请求头
        # headers = {"Content-Type": "multipart/form-data"}
        # 定义请求参数data  注意：multipart/form-data与application/json参数格式有区别
        body = MultipartEncoder({"apiKey": apiKey, "area": area, "areaID": areaID})
        # 调用get/post方法并返回响应
        return requests.post(url, headers={'Content-Type': body.content_type}, data=body)

