# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
import datetime
import re

class StudyScarpyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ArticleItemLoader(ItemLoader):
    #自定义itemloader
    default_output_processor = TakeFirst()


# 时间转换
def date_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return create_date

def return_value(value):
    return value

def remove_comment_tags(value):
    #去掉tag中提取的评论
    if "评论" in value:
        return ""
    else:
        return value

def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums

    
# 字典
class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert),
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(",")
    )
    content = scrapy.Field()


# 无测试--第四章7-15
    # def get_insert_sql(self):
    #     insert_sql = """
    #         insert into jobbole_article(title, url, create_date, fav_nums, front_image_url, front_image_path,
    #         praise_nums, comment_nums, tags, content)
    #         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE content=VALUES(fav_nums)
    #     """
    #     fron_image_url = ""
    #     # content = remove_tags(self["content"])
    #     if self["front_image_url"]:
    #         fron_image_url = self["front_image_url"][0]
    #     params = (self["title"], self["url"], self["create_date"], self["fav_nums"],
    #               fron_image_url, self["front_image_path"], self["praise_nums"], self["comment_nums"],
    #               self["tags"], self["content"])
    #     return insert_sql, params

寿司店（林旺）
由于资金不足、只能考虑夜市（位置）。

寿司饮食文化：
1、以简单为美味，以自然为美味。

第一：市场
1、寿司店林旺（藤桥）没有。
2、产品成本低，收入高。
3、夜市人流量大。
4、生活条件追求，大众化追求健康饮食。

第二：技术与设备
1、产品制作简单。
2、设备前期支出不多。

第三：市场运营
1、互联网+实体。
2、拓展式（后期投资可以进）。

第四：人员管理
1、资金足（机构培训）、招人（否则亲自教学）。
2、夜市（晚上运营、必须每天运营、除台风等特殊外）。

第五：营业估算（元）
1、最低10一份*30人流量（300）
2、一年300*30*12（10800）
3、如果按照最低标准保证盈利。
以上是最低人流量标准，不代表实际。

author：czy