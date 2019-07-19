#!/usr/bin/env python
# -*-encoding:UTF-8-*-

import requests
from retrying import retry

'''
专门请求url地址的方法
'''
headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}


@retry(stop_max_attempt_number=3) # 让修饰的函数反复被执行三次，三次全部报错之后才会报错，中间一次通过就会往下执行
def _parse_url(url):
    # 重复打印100个"*"
    print("*"*100)
    response = requests.get(url, headers=headers,timeout=5)
    return response.content.decode()

# 因为_parse_url这个方法很有可能会报错，所以需要进行try...except一下：
def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str

if __name__ == '__main__':
    # 模拟成功的情况，打印前100个字符串的情况
    url="http://www.baidu.com"
    # print(parse_url(url)[:100])

    # 模拟失败的情况
    url1 = "www.baidu.com"
    print(parse_url(url1))













