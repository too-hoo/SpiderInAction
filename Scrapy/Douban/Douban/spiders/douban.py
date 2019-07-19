# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']
    start_urls = ['http://www.douban.com/']

    def parse(self, response):
        print response.body
        pass
