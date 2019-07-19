# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiubaiItem(scrapy.Item):
    # define the fields for your item here like:
    # 作者名字
    author_name = scrapy.Field()
    # 段子内容
    content = scrapy.Field()
    # 好笑数量
    stats_vote = scrapy.Field()
    # 评论数
    comments = scrapy.Field()
    img = scrapy.Field()