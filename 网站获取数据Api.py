import json
from urllib.request import Request, urlopen

# zb网站获取数据Api
url = "https://trans.bitkk.com/line/topall?area=&jsoncallback=jQuery191025699015513536727_1530079609291&_=1530079609293"
# 包装头部
firefox_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# 构建请求
request = Request(url, headers=firefox_headers)
html = urlopen(request)
# 获取数据
data = html.read()
# 转换成字符串
strs = str(data)
# 截取字符串
print(len(strs))
strs_for_json = strs[44:]
strs_for_json = strs_for_json[:-2]
print(strs_for_json)
# 转换成JSON
data = strs_for_json
datas = json.dumps(data)
# 转换成字典数据
data_json = json.loads(data)
print(type(data_json))  # <class 'dict'>
print(data_json['datas'][0]['market'], data_json['datas'][0]['sell1Price'])
print(len(data_json['datas']))
len = len(data_json['datas'])
# 输出价格表
print("*****************************zb价格获取***************************************")
for i in range(0, len):
    print("币种\市场类型：" + data_json['datas'][i]['market'], "^^^^^^^", "实时价格：" + data_json['datas'][i]['sell1Price'],
          "^^^^^^^", "24小时最高价格：" + data_json['datas'][i]['hightPrice'], "^^^^^^^",
          "24小时最低价格：" + data_json['datas'][i]['lastPrice'])
