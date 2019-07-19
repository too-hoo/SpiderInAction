# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem
import json


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']

    baseURL = "https://careers.tencent.com/tencentcareer/api/post/Query?countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=20&language=zh-cn&area=cn"
    offset = 1
    start_urls = [baseURL.format(str(offset))]


    def parse(self, response):
    	# 使用最佳方法：页面使用js加密爬取不到，那么就爬取json类型的字符串，转换成为字典类型！
    	# 使用json.load()将json字符串转换成为python的字典类型
    	post_list = json.loads(response.body)["Data"]["Posts"]
    	for post in post_list:
    		item = TencentItem()
    		# 不能加0！
    		item["RecruitPostName"] = post["RecruitPostName"] if len(post["RecruitPostName"]) > 0 else None
    		item["BGName"] = post["BGName"] if len(post["BGName"]) > 0 else None
    		item["CountryName"] = post["CountryName"] if len(post["CountryName"]) > 0 else None
    		item["LocationName"] = post["LocationName"] if len(post["LocationName"]) > 0 else None
    		item["CategoryName"] = post["CategoryName"] if len(post["CategoryName"]) > 0 else None
    		item["LastUpdateTime"] = post["LastUpdateTime"] if len(post["LastUpdateTime"]) > 0 else None
    		item["PostURL"] = post["PostURL"] if len(post["PostURL"]) > 0 else None
    		item["Responsibility"] = post["Responsibility"] if len(post["Responsibility"]) > 0 else None
    		
    		yield item

    	if self.offset < 205:
    		self.offset += 1
    		url = self.baseURL.format(str(self.offset))
    		yield scrapy.Request(url, callback = self.parse)
    		
