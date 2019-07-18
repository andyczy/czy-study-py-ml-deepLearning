# -*- coding: utf-8 -*-
import scrapy

from cnblog.items import ArticleItem


class BlogsSpider(scrapy.Spider):
    name = 'blogs'
    allowed_domains = ['news.cnblogs.com']
    start_urls = ['https://news.cnblogs.com/']

    def parse(self, response):
        articleList = response.css('.content')

        for item in articleList:
            # 由于详情页里浏览次数是js动态加载的,无法获取,这里需要传递过去
            viewcount = item.css('.view::text').extract_first()[:-3].strip()
            detailurl = item.css('.news_entry a::attr(href)').extract_first()
            detailurl = response.urljoin(detailurl)
            yield scrapy.Request(url=detailurl, callback=self.parse_detail, meta={"viewcount": viewcount},
                                 dont_filter=True)
        # 获取下一页标签
        text = response.css('#sideleft > div.pager > a:last-child::text').extract_first().strip()
        if text == 'Next >':
            next = response.css('#sideleft > div.pager > a:last-child::attr(href)').extract_first()
            url = response.urljoin(next)

            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    ##解析详情页内容
    def parse_detail(self, response):
        article = ArticleItem()
        article['title'] = response.css('#news_title a::text').extract_first()
        article['viewcount'] = response.meta["viewcount"]
        article['content'] = response.css('#news_body').extract_first("")
        yield article
