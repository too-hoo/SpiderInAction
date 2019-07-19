#!/usr/bin/env python
# -*-encoding:UTF-8-*-

import requests

url = "https://www.douban.com"

headers = {
'Cookie': 'll="118281"; bid=0Db7R9i94K4; _pk_ses.100001.8cb4=*; __utma=30149280.1425071208.1562572605.1562572605.1562572605.1; __utmc=30149280; __utmz=30149280.1562572605.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ap_v=0,6.0; __yadk_uid=hwni9KvD0d2cdckeVV4zz9DqCFvMu88S; push_noty_num=0; push_doumail_num=0; __utmv=30149280.15209; dbcl2="152090813:uQSEnc0h6Mk"; ck=PZj4; __utmt=1; _pk_id.100001.8cb4=ad891105c19efa78.1562572600.1.1562573931.1562572600.; __utmb=30149280.24.9.1562573932605',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

response = requests.get(url, headers=headers)

# 将豆瓣的首页写入到文件
with open("douban2.html","w", encoding="UTF-8") as f:
    f.write(response.content.decode("UTF-8"))
























