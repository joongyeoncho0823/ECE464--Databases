# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient

class MyscraperPipeline(object):
    
    def __init__(self):
        self.conn = MongoClient(
    "mongodb+srv://ece464p2_admin:ece464p2_ADMIN@cluster0.m5b08.mongodb.net/admin")
        db = self.conn['scraper']
        self.collection = db['books']


    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
