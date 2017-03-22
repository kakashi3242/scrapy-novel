# -*- coding: utf-8 -*-
import scrapy
from Novel.items import NovelItem


class NovelcontentSpider(scrapy.Spider):
    name = "novelContent"
    allowed_domains = ["69shu.com"]
    start_urls = [
        'http://www.69shu.com/txt/8894/13563698'
    ]

    def parse(self, response):
        page = '/html/body/div[2]/table/tbody/tr/td'
        domain = 'http://www.69shu.com'
        for con in response.xpath(page):
            item = NovelItem()
            item['title'] = con.xpath('h1/text()').extract()
            href = con.xpath('div[2]/span[4]/a/@href').extract()
            item['href'] = domain + href[0]
            item['content'] = con.xpath('div[1]/text()').extract()

            fo = open('《邪王追妻：废材逆天小姐》.txt',mode = 'a',encoding = 'utf-8')
            titleNew = str(item['title'][0]).split('.')
            fo.write(titleNew[1]+'\n')
            for content in item['content']:
                book_content = str(content).replace('\xa0\xa0\xa0\xa0','    ')
                book_content = book_content.replace('\r\n','\n')
                fo.write(book_content)
            fo.write('\n'+'\n')
            fo.close()

            yield item

        nextPage = response.xpath('/html/body/div[2]/table/tbody/tr/td/div[2]/span[4]/a/@href').extract()
        if nextPage:
            nextUrl = domain + nextPage[0]
            self.log(nextUrl)
            yield scrapy.http.Request(nextUrl,callback=self.parse)
