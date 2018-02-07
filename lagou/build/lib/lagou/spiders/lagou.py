import scrapy
from scrapy.spider import Spider
class lagou(scrapy.Spider):
    name="lagou";
    start_urls=[
        "https://www.lagou.com/zhaopin/"
    ]
    def parse(self,response):
        print("---------------")
        # print(response.body.decode());
        for item in response.css(".p_top a"):
            title=item.css("h3::text");
            print(title);
