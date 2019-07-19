#!/usr/bin/env python
# -*-encoding:UTF-8-*-

import requests
import json  # 内建模块，直接导入即可

url = "https://fanyi.baidu.com/basetrans"
# 请求头需要加上cookie和user-agent才行，以后可能会更加严格
headers = {
"cookie": "BAIDUID=6C044A831E6FD254BC0554549DBDE2F7:FG=1; BIDUPSID=6C044A831E6FD254BC0554549DBDE2F7; PSTM=1562555922; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; H_PS_PSSID=1422_21101_29074_29238_28519_29098_28839_29220_20719; PSINO=7; locale=zh; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1562567374; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1562567374; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1562563594,1562563674,1562567375; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1562567375; yjs_js_security_passport=c5b15d8195235a9d3f78ced8984f8915b39ec00c_1562567398_js",
"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
query_str = input("请输入需要翻译的内容：") # "人生苦短，我用python" 对应的字符串进行了加密，只能输入这个了
# 更改翻译内容之后token和sign的值都会改变，这样就能够反爬虫了
# 就是在客户端根据输入的内容使用保密的算法生成一个token，例如md5或者sha256等摘要算法都是可以的，达到反爬虫的目的
data = {"query": query_str,
                "from": "zh",
                "to": "en",
                "token": "7997ec08066e6595e5a90ef208e48d6a",
                "sign": "289133.35420"} # 已经使用js对翻译的字符串进行加密了
response = requests.post(url, data=data, headers=headers)

html_str = response.content.decode() # 接收json格式的字符串

dict_ret = json.loads(html_str)
print(dict_ret)
# 会显示是字符串的类型的数据，就是json类型的数据
print(type(dict_ret))  # 类型变成dict<class 'dict'>
# 获取字典里面的翻译的结果：操作字典
result = dict_ret["trans"][0]["dst"]
print("翻译的结果是："+ result)