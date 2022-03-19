import json


# 新建读取文件类
class ReadFile(object):
    def __init__(self, filename):
        self.filepath = "../data/" + filename

    # 新建读取文件方法
    def read_file(self):
        # 打开文件
        with open(self.filepath, "r", encoding="utf-8") as f:
            # 读取文件流
            return json.load(f)


if __name__ == '__main__':
    datas = ReadFile("param.json").read_file()
    print(datas)
    # 新建空列表
    arr = []
    # 遍历获取所有的value：dict.values()
    for data in datas.values():
        arr.append((data.get("url"),
                    data.get("apiKey"),
                    data.get("area"),
                    data.get("areaID"),
                    data.get("expected"),
                    data.get("status_code")
                    ))
        print(arr)
