# -*- coding: utf-8 -*-
import scrapy
from myDouban.items import MydoubanItem
# from scrapy.Request import Request


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']

    start_urls = ['https://www.douban.com/']

    def parse(self, response):
        for item in response.css(".group-cate ul li a"):
            title=item.xpath("text()").extract()[0];
            href=item.xpath("@href").extract()[0];
            onetime=MydoubanItem();
            onetime["title"]=title;
            onetime["href"]=href;
            yield onetime

        #     yield Request(url=item_details_url, meta={'item': item},callback=self.parse_details)
        # def parse_details(self,response):
        #     print("***********************************")