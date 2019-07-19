# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyu.com']
    baseURL = "https://m.douyu.com/api/room/list?page={}&type=yz"
    offset = 1
    start_urls = [baseURL.format(str(offset))]

    def parse(self, response):
    	data_list = json.loads(response.body)["data"]["list"]
    	if not len(data_list):
    		return
    	for data in data_list:
    		item = DouyuItem()
    		item["nickname"] = data["nickname"] if len(data["nickname"]) > 0 else None
    		item["imagelink"] = data["verticalSrc"] if len(data["verticalSrc"]) > 0 else None
    		yield item

    	# 记得加yield！ rm * 删除当前文件夹下的所有文件
    	self.offset += 1
    	yield scrapy.Request(self.baseURL.format(str(self.offset)),
    		callback=self.parse)
