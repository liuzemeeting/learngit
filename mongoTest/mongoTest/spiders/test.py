# -*- coding: utf-8 -*-
import scrapy
from pymongo import MongoClient
from mongoTest.items import MongotestItem
from scrapy import Request

myhead={
    
}


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://flights.ctrip.com/booking/XMN-BJS-day-1.html?DDate1=2016-04-19']
    db=MongoClient("127.0.0.1",27017)
    mydb=db["hua"];
    person=mydb["person"]
    # person.insert({'title':'gogogogoo'})
    print(person)
    def parse(self, response):
        print(response.body.decode())
        # xiecheng="http://flights.ctrip.com/booking/XMN-BJS-day-1.html?DDate1=2016-04-19"
        # request=Request(xiecheng,headers=None,callback=self.parseResult)
        print("---------------------------------------------------------------")
        for item in response.css(".J_header_row"):
            print("*********************************----------------")
            company=item.xpath("./td[1]/div[1]/strong/text()").extract();
            planeType=item.xpath("./td[1]/div[2]/span/text()").extract();
            airNumber=item.xpath("./td[1]/div[1]/span/text()").extract();
            print(company)
            print(planeType);
            print(airNumber)
            
            
        pass;
    print(person)
