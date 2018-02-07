# from scrapy.exporters import JsonLinesItemExporter
from scrapy import signals
# from scrapy.extensions.feedexport import *
# class superspider(object):
#     print("-------------------------------------")
#     def __init__(self):
#         print("开始爬取.........");
#         self.exporter=JsonLinesItemExporter(self.myFile , ensure_ascii=False);


from scrapy.exporters import JsonLinesItemExporter


class superspider(object):
    # def __init__(self, file, **kwargs):
    #     super(chongxie , self).__init__(file , ensure_ascii=None);
    
    def spider_opened(self, spider):
        print("开始爬取。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。");
        self.myFile = open("shuju.json" , "wb");
        self.exporter = JsonLinesItemExporter(self.myFile , ensure_ascii=False)

        # 开始导出数据
        self.exporter.start_exporting();



    def spider_closed(self, spider):
        print("爬取关闭。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。");

        self.exporter.finish_exporting();
        self.myFile.close();
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls();
        crawler.signals.connect(pipeline.spider_opened , signals.spider_opened);
        crawler.signals.connect(pipeline.spider_closed , signals.spider_closed);
        return pipeline;

    def process_item(self , item , spider):
        self.exporter.export_item(item);
        return item;
