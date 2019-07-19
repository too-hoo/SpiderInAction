# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import scrapy
from settings import IMAGES_STORE as images_store # 同级，直接到入就可以
from scrapy.pipelines.images import ImagesPipeline

class DouyuPipeline(ImagesPipeline):
    
    def get_media_requests(self, item, info): # 重写管道里面的这个方法，此方法返回一个请求
	#1、spider那边拿到图片的link，通过item穿过来这个方法，这个方法在进行请求，获取到图片
	#bug 神奇的格式
	image_link = item['imagelink']
        yield scrapy.Request(image_link)

        #2、setting.py里面存在一个参数IMAGES_STORE，这个参数指定图片的存放路径
        #3、同时开启管道，手机端的需要给个useragent，模拟手机，关闭robot协议，设置为false
        #4、导入scrapy和ImagesPipeline


    #5、更改图片的名称
    #6、当下载不来文件的时候，对文件重命名时会提示错误
    def item_completed(self, results, item, info):
    	# print results
    	# print "*" * 30
    	# 当打印记过的时候会返回这个值，我们要更改获取到的图片的名称，就要获取到需要修改的图片的名字
    	# [(True, {'url': 'https://rpic.douyucdn.cn/live-cover/appCovers/2019/06/05/6135669_20190605182649_big.jpg', 'path': 'full/fc1690ef4f09f31c166a16b5836887116a88ce11.jpg', 'checksum': '8d177f1dc45250ced6feff6e30b4003e'})]	
    	image_path = [x["path"] for ok,x in results if ok] # 意思就是使用ok和x迭代results，ok代表上面的true，只有ok=true的时候，我们才能取到path的值
    	# 使用os，获取到文件存放的路径，在settings.py里面，修改(前旧后新)，通过checksum的md5值来找到原来的图片
    	# 因为image_path是一个列表，所以需要使用image_path[0]提取里面的元素
    	os.rename(images_store + image_path[0], images_store + item["nickname"].encode("utf-8") + '.jpg')
    	return item

    
