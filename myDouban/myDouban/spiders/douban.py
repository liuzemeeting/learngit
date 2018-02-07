# -*- coding: utf-8 -*-
import scrapy
from myDouban.items import MydoubanItem
# from scrapy.Request import Request


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']

    start_urls = ['https://music.douban.com/chart']

    def parse(self, response):
        print("]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
        print(response.body.decode())
        for item in response.css(".intro-play"):
            title=item.xpath("p/text()").extract()[0];
            href=item.xpath("::h3/text").extract()[0];
            onetime=MydoubanItem();
            onetime["title"]=title;
            onetime["href"]=href;
            yield onetime

        #     yield Request(url=item_details_url, meta={'item': item},callback=self.parse_details)
        # def parse_details(self,response):
        #     print("***********************************")