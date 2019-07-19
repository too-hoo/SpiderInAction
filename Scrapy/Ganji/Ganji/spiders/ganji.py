# -*- coding: utf-8 -*-
import scrapy
from Ganji.items import GanjiItem

class GanjiSpider(scrapy.Spider):
    name = 'ganji'
    allowed_domains = ['gz.ganji.com'] # 注意这里的域名要打于start_urls的域名
    # start_urls = ['http://gz.ganji.com/zpjisuanjiwangluo/zhaopin/o{}'.format(i) for i in range(1,8)]
    baseURL = "http://gz.ganji.com/zpjisuanjiwangluo/zhaopin/o"
    offset = 1
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
    	#1、获取到所有的列表
    	dl_list = response.xpath("//dl[@class='list-noimg job-list clearfix new-dl']")
    	#2、分组获取
    	for content in dl_list:
    		item = GanjiItem()
    		item["recruit_title"] = content.xpath(".//a[@class='list_title gj_tongji']/text()").extract()
    		item["recruit_title"] = item["recruit_title"][0].strip() if len(item["recruit_title"]) > 0 else None
    		item["company"] = content.xpath(".//div[@class='new-dl-company']/a/text()").extract()
    		item["company"] = item["company"][0] if len(item["company"]) > 0 else None
    		item["location"] = content.xpath(".//dd[@class='pay']/text()").extract()
    		item["location"] = item["location"][0] if len(item["location"]) > 0 else None
    		item["salary"] = content.xpath(".//div[@class='new-dl-salary']/text()").extract()
    		item["salary"] = item["salary"][0].strip() if len(item["salary"]) > 0 else None
    		item["publish_time"] = content.xpath(".//dd[@class='pub-time']/span/text()").extract()
    		item["publish_time"] = item["publish_time"][0] if len(item["publish_time"]) > 0 else None
    		item["treatment"] = content.xpath(".//div[@class='new-dl-tags']//i/text()").extract()
    		item["treatment"] = item["treatment"][0].strip() if len(item["treatment"]) > 0 else None
    	
    		yield item

    	# if self.offset < 350:
    	# 	self.offset += 1
    	# 	url = self.baseURL + str(self.offset)
    	# 	yield scrapy.Request(url, callback = self.parse)

    	if len(response.xpath("//ul[@class='pageLink clearfix']//a[@class='next']")):
    		url = response.xpath("//a[@class='next']/@href").extract()[0]
    		yield scrapy.Request("http://gz.ganji.com/" + url, callback = self.parse)




        
