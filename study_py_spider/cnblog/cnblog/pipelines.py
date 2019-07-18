# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class itemPipeline(object):
    def __init__(self):
        self.filename = open("cnblog.json", "wb")

    def process_item(self, item, spider):
        data = ''
        title = item['title']
        link = item['link']
        name = item['name']
        for i, j, k in zip(title, name, link):
            data += '用户名：' + '_' + i + '_' + j + '_' + k + '\n'
        self.filename.write(data.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.filename.close()


class articlePipeline(object):
    def __init__(self):
        self.filename = open("article.json", "wb")

    def process_item(self, item, spider):
        title = item['title']
        content = item['content']
        viewcount = item['viewcount']
        # self.filename.write(title,viewcount,content)
        return item

    def close_spider(self, spider):
        self.filename.close()
