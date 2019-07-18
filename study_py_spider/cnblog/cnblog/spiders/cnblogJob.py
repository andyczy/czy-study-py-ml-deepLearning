# -*- coding: utf-8 -*-
import scrapy
from cnblog.items import CnblogItem

class CnblogjobSpider(scrapy.Spider):
    name = 'cnblogJob'
    allowed_domains = ['cnblog.com']
    start_urls = ['https://www.cnblogs.com/']

    def parse(self, response):
        item = CnblogItem()
        item['title'] = response.xpath('//a[@class="titlelnk"]/text()').extract()
        item['link'] = response.xpath('//a[@class="titlelnk"]/@href').extract()
        item['name'] = response.xpath('//div[@class="post_item_foot"]/a/text()').extract()

        yield item