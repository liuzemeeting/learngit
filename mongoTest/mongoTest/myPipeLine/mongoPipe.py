from scrapy.conf import settings
from pymongo import MongoClient

# MONGO_HOST
# MONGO_PORT
# MONGO_DBNAME
# MONGO_COLLECTION
class mongopipeclass(object):
    def __init__(self):
        print("********************************************")
        client=MongoClient(settings["MONGO_HOST"],settings["MONGO_PORT"])
        mydb=client[settings["MONGO_DBNAME"]]
        self.collection=mydb[settings["MONGO_COLLECTION"]]
        
    
    def process_item(self,item,spider):
        print("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}")

        self.collection.insert({"name":item["title"]})

        return item;
