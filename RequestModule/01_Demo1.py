#!/usr/bin/env python
# -*-encoding:UTF-8-*-

import requests

url = "http://www.baidu.com"
# 爬去百度的首页只需要使用user-Agent就行
headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
response = requests.get(url,headers=headers)
# print(response)
# 直接打印会出现乱码,需要进行编码
# response.encoding="UTF-8"
# print(response.text)

# 获取网页的HTML内容,直接输出会产生byte类型的内容，需要进行解码.decode()
# print(response.content.decode())

# response的一些方法的测试
print(response.request.url)
print(response.url)
print(response.request.headers)
print(response.headers)
