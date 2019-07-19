#!/usr/bin/env python
# -*- coding:utf-8 -*-


from lxml import html
import requests

# 由于python3.7中安装lxml之后已经没有etree模块了，所以需要这样使用
etree = html.etree

url="https://movie.douban.com/chart"

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

response = requests.get(url, headers=headers)
html_str = response.content.decode()
# print(html_str)

# 使用etree处理数据,注意这里使用html_new,不要使用html，否则会和导入的html冲突！
html_ret = etree.HTML(html_str)
# 打印出的是一个对象
print(html_ret)

# 写xpath的时候需要根据url的真实相应来写，最直接的就是对比，打开网页的源代码，对比代码和Element的内容，然后得出xpath的写法。
# 因为可能会是广告，不存在的。
# 1、获取所有的电影的url地址
url_list = html_ret.xpath("//div[@class='indent']/div/table//div[@class='pl2']/a/@href")
# print(url_list)

# 2、获取所有的图片的地址
img_list = html_ret.xpath("//div[@class='indent']/div/table//a[@class='nbg']/@href")
# print(img_list)

# 3、需求把每部电影组成一个字典，字典中是电影的更新数据，比如标题，url，图片地址，评论数，评分
# 思路：
    # 1、分组
    # 2、每一组提取数据

ret1 = html_ret.xpath("//div[@class='indent']/div/table")
# print(ret1)
# 遍历列表中的每一个元素
for table in ret1:
    item = {}
    item["title"] = table.xpath(".//div[@class='pl2']/a/text()")[0].replace("/","").strip()
    item["url"] = table.xpath(".//div[@class='pl2']/a/@href")[0]
    item["img_url"] = table.xpath(".//a[@class='nbg']/@href")[0]
    item["comment"] = table.xpath(".//div[@class='star clearfix']/span[@class='pl']/text()")[0]
    item["rating"] = table.xpath(".//div[@class='star clearfix']/span[@class='rating_nums']/text()")[0]
    print(item)












