



#!/usr/bin/env python
# -*-encoding:UTF-8-*-

import requests
from retrying import retry

'''
专门请求url地址的方法
'''
# headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

# cookie容易超时，需要更新;另外cookie的值里面的双引号不能改，外面单引号，里面双引号
headers = {
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
'Cookie': 'bid=6yrd9Sx5qkk; douban-fav-remind=1; gr_user_id=82a14c13-70aa-472f-a275-2d1f69dd758e; _vwo_uuid_v2=D646C9FD23C561F2DEBB02283DDBF8801|1d7619d63f531df5e42890c9d0e9258d; viewed="1231584_24529132"; ll="118281"; push_noty_num=0; push_doumail_num=0; Hm_lvt_6d4a8cfea88fa457c3127e14fb5fabc2=1563064550; _ga=GA1.2.889532456.1550338671; _gid=GA1.2.10888675.1563064728; _ga=GA1.3.889532456.1550338671; _gid=GA1.3.10888675.1563064728; __utmc=30149280; dbcl2="152090813:dZQg55aV0rA"; ck=snv5; __utmv=30149280.15209; frodotk="75ad95cec41872ba6108c16c4c49582e"; talionusr="eyJpZCI6ICIxNTIwOTA4MTMiLCAibmFtZSI6ICJcdTgyYjFcdTUxM2ZcdTcyMzFcdTRlMmRcdTU2ZmQifQ=="; ap_v=0,6.0; __utma=30149280.889532456.1550338671.1563075836.1563083146.9; __utmz=30149280.1563083146.9.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lpvt_6d4a8cfea88fa457c3127e14fb5fabc2=1563086800',
'Referer': 'https://m.douban.com/tv/chinese'
}


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







