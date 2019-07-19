# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class TencentPipeline(object):
	
    def __init__(self):
	# 初始化一次之后就不会再执行，将数据写到文件里面去（可选）
	# 首先第一个item过来之后会调用这个方法
	# vim显示的不同，bug，这样的格式才能正确在Linux上显示，可能是__init__函数的问题
	self.f = open("tencent_pipeline.json","w")

    def process_item(self, item, spider): # 每次处理item的时候都会调用这个方法
    	#1、因为传入的item并不是真正的字典，所以需要强转一下
    	content = json.dumps(dict(item),ensure_ascii = False) + ",\n"
    	#2、写入到json文件里面去
    	self.f.write(content.encode("utf-8"))
    	#3、返回item给引擎
        return item

    def close_spider(self,spider):
    	# 最后关闭打开的文件(打开文件之后需要关闭)
    	self.f.close()
