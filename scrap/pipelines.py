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
        """Constructor"""
        self.create_connection()
        self.create_table()

    def create_connection(self):
        """Create a connection to the database"""
        self.cnt = sqlite3.connect('db.sqlite3')
        self.cur = self.cnt.cursor()

    def create_table(self):
        """"Create a table in the database"""
        self.cur.execute("""CREATE TABLE IF NOT EXISTS myapp_company (companyName textl,ricCode text)""")

    def store_data(self, item):
        """Store data in the database"""
        self.cur.execute("""INSERT INTO myapp_company (companyName,ricCode)VALUES(?,?);""",
                         (item['companyName'], item['ricCode']))
        self.cnt.commit()

    def process_item(self, item, spider):
        """Process the item"""
        self.store_data(item)
        return item
