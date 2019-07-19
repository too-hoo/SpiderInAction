



#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from lxml import html
import json
etree = html.etree

class QiubaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/hot/page/{}/"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    def get_url_list(self):
        # 根据url地址的规律，构造url list, 不是使用while，而是使用for
        url_list = [self.url_temp.format(i) for i in range(1, 14)]
        return url_list

    def parse_url(self,url):
        print("now parsing:" + url)
        # response = requests.get(url,headers=self.headers)
        # 好像不需要headers也行
        response = requests.get(url)
        return response.content.decode()

    def get_content_list(self, html_str):
        # 使用lxml工具
        html_ret = etree.HTML(html_str)
        # 1、获取到所有的段子的列表
        div_list = html_ret.xpath("//div[@id='content']//div[@id='content-left']/div")
        content_list = []
        # 2、分组处理：
        for content in div_list:
            item = {}
            item["author_name"] = content.xpath(".//div[@class='author clearfix']/a/h2/text()")
            item["author_name"] = item["author_name"][0].strip() if len(item["author_name"]) > 0 else None
            item["content"] = content.xpath(".//div[@class='content']/span/text()")
            item["content"] = item["content"][0].strip() if len(item["content"]) > 0 else None
            item["stats-vote"] = content.xpath(".//div[@class='stats']/span[@class='stats-vote']/i/text()")
            item["stats-vote"] = item["stats-vote"][0] if len(item["stats-vote"]) > 0 else None
            item["comments"] = content.xpath(".//a[@class='qiushi_comments']/i/text()")
            item["comments"] = item["comments"][0] if len(item["comments"]) > 0 else None
            item["img"] = content.xpath(".//div[@class='thumb']/a/img/@src")
            item["img"] = "https" + item["img"][0] if len(item["img"]) > 0 else None
            content_list.append(item)
        return content_list


    def save_content_list(self, content_list): # 保存
        with open("qiubai.json","a", encoding="UTF-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False)) # 最后换行的时候不用退两格，直接在一行显示即可
                f.write("\n")
        print("保存成功！")


    def run(self): # 实现主要逻辑
        # 1、根据url地址的规律，构造url list
        url_list = self.get_url_list()
        # 2、发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3、提起数据
            content_list = self.get_content_list(html_str)
            # 4、保存
            self.save_content_list(content_list)

if __name__ == '__main__':
    qiubai = QiubaiSpider()
    qiubai.run()


