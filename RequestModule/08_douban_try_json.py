#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
from parse import parse_url


# 爬豆瓣的数据:不知道为什么在Ubuntu里面使用不了豆瓣的手机版！
# 删掉&type=jsonp&dataType=jsonp和callback=xxx，否则它返回的是xxx(json格式)的字符串或者以jsonp(json格式)格式的字符串
class DoubanSpider:
    def __init__(self):
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_domestic/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=0"

    def get_content_list(self,html_str):
        # 获取数据
        dict_data = json.loads(html_str)
        # 并不是要获取所有的数据，我们只需获取对应的主要的数据即可
        content_list = dict_data["subject_collection_items"]
        # 获取total的值
        total = dict_data["total"]
        return content_list, total

    def save_content_list(self, content_list):
        # 注意这里的写文件的方法，“a”表示如果文件不存在就创建，并且只能进行写操作，不会覆盖，从后面追加
        # 如果是使用“w”方法的话，会不断的覆盖的，文件最后什么内容都没有。
        with open("douban.json","a",encoding="UTF-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功！")

    # 此方法实现主要逻辑
    def run(self):
        num = 0
        total = 10
        while num < total + 18:
            # 1、start_url
            url = self.temp_url.format(num)
            print(url)
            # 2、发送请求，获得响应
            html_str = parse_url(url)
            # 3、提取数据,注意这里使用self进行调用！
            content_list, total = self.get_content_list(html_str)
            # 4、保存
            self.save_content_list(content_list)
            # 5、构造下一页的url地址，循环2-5步
            num += 18


# 运行程序，实例化对象
if __name__ == '__main__':
    douban = DoubanSpider()
    douban.run()















