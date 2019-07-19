# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GanjiItem(scrapy.Item):
    # define the fields for your item here like:
    recruit_title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    salary= scrapy.Field()
    publish_time = scrapy.Field()
    treatment = scrapy.Field()