#!/usr/bin/env python
# -*-encoding:UTF-8-*-

import requests

session = requests.session()


# 先发送post请求，获取cookie，然后带上cookie请求登录后的页面
# 有的网站登录是不会有action这个字段的，需要使用network进行抓包，在此之前需要进行Preserve log的勾选，保留log避免清空
# 例如豆瓣的一级post请求是不会找到action，
post_url = "https://accounts.douban.com/j/mobile/login/basic"
headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
post_data = {"name":"12345678909", "password":"12345678909"}
session.post(post_url, data=post_data, headers=headers)

# 获取到cookie之后进行对登陆后的页面请求
url = "https://www.douban.com"
response = session.get(url, headers=headers)

with open("douban4.html", "w", encoding="UTF-8") as f:
    f.write(response.content.decode("UTF-8"))























