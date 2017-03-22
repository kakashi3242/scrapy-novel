# -*- coding: utf-8 -*-
import scrapy
from Novel.items import NovelItem


class XiewangSpider(scrapy.Spider):
    name = "xiewang"
    allowed_domains = ["69shu.com"]
    start_urls = [
        'http://www.69shu.com/8894/'
        ]

    def parse(self, response):
        titleList = '/html/body/div[2]/div[4]/ul/li'
        domain = 'http://www.69shu.com'
        for con in response.xpath(titleList):
            item = NovelItem()
            item['title'] = con.xpath('a/text()').extract()
            href = con.xpath('a/@href').extract()
            item['href'] = domain + href[0]
            yield item
