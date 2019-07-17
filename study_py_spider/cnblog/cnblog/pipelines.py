# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FilePipeline(object):

    def process_item(self, item, spider):
        data = ''
        with open('cnblog.txt', 'w', encoding='utf-8') as f:
            titles = item['title']
            links = item['link']
            name = item['name']
            for i, j, k in zip(titles, links, name):
                data += '用户名：' + k + ' <> ' + i + ':' + j + '\n'
            f.write(data)
            f.close()
        return item
