# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class QiubaiPipeline(object):	
    def __init__(self):
	# 初始化一次之后就不再执行，将数据写到文件里面去（可选）
	#一个item过来
	self.f = open("qiubai_pipeline.json", "w")

	# 这个方法是默认生产的，管道就是由来出来传过来的item的，一模一样，名字不一样也是它
    def process_item(self, item, spider):
    	# 将python的字典转换成为字符串存储到本地,因为传入的item不是真正字典所以需要强转一下
    	content = json.dumps(dict(item),ensure_ascii = False) + ",\n"
    	# 写入到json文件里面去
    	self.f.write(content.encode("utf-8"))
    	# 如果有多个管道就交给下一个管道，最后没有管道才交给引擎
    	# 一定要返回到引擎，告诉引擎我处理完了，给我下一个item吧
        return item

    def close_spider(self,spider):
    	# 最后关闭打开的文件（打开文件之后要关闭）
    	self.f.close()
