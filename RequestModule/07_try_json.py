#!/usr/bin/env python
# -*-encoding:UTF-8-*-

import requests
import json  # 内建模块，直接导入即可

# 爬淘宝的数据
# 删掉&type=jsonp&dataType=jsonp和callback=xxx，否则它返回的是xxx(json格式)的字符串或者以jsonp(json格式)格式的字符串
url = "https://acs.m.taobao.com/h5/mtop.taobao.wsearch.h5search/1.0/?jsv=2.3.16&appKey=12574478&t=1563070543334&sign=4bb4db9d4f5969c25a3ae5ec00a4d57d&api=mtop.taobao.wsearch.h5search&v=1.0&H5Request=true&ecode=1&AntiCreep=true&AntiFlool=true&data=%7B%22event_submit_do_new_search_auction%22%3A%221%22%2C%22_input_charset%22%3A%22utf-8%22%2C%22topSearch%22%3A%221%22%2C%22atype%22%3A%22b%22%2C%22searchfrom%22%3A%221%22%2C%22action%22%3A%22home%3Aredirect_app_action%22%2C%22from%22%3A%221%22%2C%22q%22%3A%22%E5%A8%83%E5%A8%83%22%2C%22sst%22%3A%221%22%2C%22n%22%3A20%2C%22buying%22%3A%22buyitnow%22%2C%22m%22%3A%22api4h5%22%2C%22token4h5%22%3A%22%22%2C%22abtest%22%3A%2258%22%2C%22wlsort%22%3A%2258%22%2C%22page%22%3A1%7D"


# cookie容易超时，需要更新
headers = {
"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
"cookie": "cna=txvtFDjNACACATr8gw4HrP4t; UM_distinctid=168fcc45f02be-0bf7199faa9b8-b781636-100200-168fcc45f0427e; thw=cn; tracknick=%5Cu5403%5Cu5C4E%5Cu54271; tg=0; enc=deGI2kD9HPChYnn8jUq3X1WUu8rWILKOVj2EwhtC5oVpDgMDErBAxuMMHQ1m5LMIBr8zxNyCf0%2FaSci%2FGONS0w%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; miid=207788181508495554; t=17d35bf33bc5cdffa4815a34fbcc7492; lgc=%5Cu5403%5Cu5C4E%5Cu54271; uc3=vt3=F8dBy3kdrB7oEpw0nW0%3D&id2=UNX6w78eNduX&nk2=0OTLAOpfEQ%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D; _cc_=VFC%2FuZ9ajQ%3D%3D; l=bBPgpRiPvFS_qtR1BOCwCuI8aPbOSIRYSuPRwNcXi_5IA6Ts0T_Okm9bFF96Vj5RsLYB4z6vzNp9-etkw; _m_h5_tk=ae1fdf7adcf44232505b4f4e07646b0d_1563077421638; _m_h5_tk_enc=10643209dee46cf4f0fa0649a82aef50; cookie2=1680e460548af7b25ab8d052cb557995; _tb_token_=3e756e713afb8; isg=BF9fYrbkfjwtB3tiqAHbHS5k7rMpbLMDeueBUvGs-45VgH8C-ZRDtt1RRhD-IIve",
"referer": "https://s.m.taobao.com/h5?event_submit_do_new_search_auction=1&_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&action=home%3Aredirect_app_action&from=1&sst=1&n=20&buying=buyitnow&q=%E5%A8%83%E5%A8%83"
}

response = requests.get(url, headers=headers)
json_str = response.content.decode()

# 将json字符串解析成为字典类型，
ret1 = json.loads(json_str)
print(type(ret1))

# 将字典类型的Python字符转换成为本地文件保存
with open("taobao.txt","w",encoding="UTF-8") as f:
    # f.write(json.dumps(ret1)) 这样直接写的话会出现中文解析不出来，需要使用一个字段ensure_ascii = false
    # 需要在解析的时候忽略ascii编码，使得保持中文显示，但是是一行显示，看起来还是不好看
    # f.write(json.dumps(ret1,ensure_ascii=False))
    # 需要使用dumps里面的第三个参数，indent=2,就是每一行换行是空两格，这样看起来就好看了
    f.write(json.dumps(ret1, ensure_ascii=False, indent=2))

