# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


from pymongo import MongoClient
client = MongoClient()
collection = client["name"]


class DemopipLine(object):
    # 爬虫开启执行一次
    def open_spider(self, spider):
        self.file = open(spider.settings.get("SAVE_FILE","./temp.json"), "w")

    # 爬虫关闭执行一次
    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        print(item)
        return item                         # 不return等级低的pipLine不能获取到item