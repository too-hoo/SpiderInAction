# -*- coding: utf-8 -*-
import scrapy
from  QiuBai.items import QiubaiItem


class QiubaispiderSpider(scrapy.Spider):
	# 爬虫的名称，启动爬虫时需要的参数（必需）
    name = 'QiuBaiSpider'
    # 爬取域范围，允许爬虫在这个域名下进行爬取（可选）
    allowed_domains = ['www.qiushibaike.com']
    # 起始url列表，爬虫执行后的第一批请求，将从这个列表中获取
    start_urls = ['https://www.qiushibaike.com/hot/page/{}/'.format(i) for i in range(1, 14)]

    def parse(self, response):
    	# 1、获取到所有的段子的列表
        div_list = response.xpath("//div[@id='content']//div[@id='content-left']/div")
        # content_list = []
        # 2、分组处理：
        for content in div_list:
            # 这里需要用上导入的QiubaiItem
            # 记得需要加上extract()，返回一个list,否则报错：TypeError: <Selector xpath= ... is not JSON serializable
            # TypeError: <Selector xpath=".//div[@class='author clearfix']/a/h2/text()" data=u'\n\u996e\u6700\u70c8\u7684\u9152\u3001\u8279\u6700\u7231\u2026\n'> is not JSON serializable
            item = QiubaiItem()
            item["author_name"] = content.xpath(".//div[@class='author clearfix']/a/h2/text()").extract()
            item["author_name"] = item["author_name"][0].strip() if len(item["author_name"]) > 0 else None
            item["content"] = content.xpath(".//div[@class='content']/span/text()").extract()
            item["content"] = item["content"][0].strip() if len(item["content"]) > 0 else None
            item["stats_vote"] = content.xpath(".//div[@class='stats']/span[@class='stats-vote']/i/text()").extract()
            item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"]) > 0 else None
            item["comments"] = content.xpath(".//a[@class='qiushi_comments']/i/text()").extract()
            item["comments"] = item["comments"][0] if len(item["comments"]) > 0 else None
            item["img"] = content.xpath(".//div[@class='thumb']/a/img/@src").extract()
            item["img"] = "https:" + item["img"][0] if len(item["img"]) > 0 else None
            # 返回提取到的每一个item数据，给管道文件进行处理，同时还会返回回来继续执行后面的代码
            yield item

           