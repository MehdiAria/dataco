# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class ScrapPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.cnt = sqlite3.connect('dataco.db')
        self.cur = self.cnt.cursor()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS company (companyName textl,ricCode text)""")

    def store_data(self, item):
        self.cur.execute("""INSERT INTO company (companyName,ricCode)VALUES(?,?);""",
                         (item['companyName'], item['ricCode']))
        self.cnt.commit()

    def process_item(self, item, spider):
        self.store_data(item)
        return item
