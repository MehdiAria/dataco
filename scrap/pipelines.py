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
from .items import EsgItem, ScrapItem


class Pipeline(object):
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
        pass

    def store_data(self, item):
        """Store data in the database"""
        pass

    def process_item(self, item, spider):
        """Process the item"""
        # if isinstance(item, EsgItem):
        #     print('ESG','$'*100000)
        # if isinstance(item, ScrapItem):
        #     print('ScrapItem','$'*100000)
        try:
            self.store_data(item)
        except KeyError as e:
            # raise e
            pass
        return item


class ScrapPipeline(Pipeline):
    def __init__(self):
        super().__init__()

    def create_connection(self):
        super().create_connection()

    def create_table(self):
        """"Create a table in the database"""
        self.cur.execute("""CREATE TABLE IF NOT EXISTS myapp_company (companyName text,ricCode text)""")

    def store_data(self, item):
        """Store data in the database"""
        self.cur.execute("""INSERT INTO myapp_company (companyName,ricCode)VALUES(?,?);""",
                         (item['companyName'], item['ricCode']))
        self.cnt.commit()

    def process_item(self, item, spider):
        return super().process_item(item, spider)


class EsgPipeline(Pipeline):
    def __init__(self):
        super().__init__()

    def create_connection(self):
        super().create_connection()

    def create_table(self):
        """"Create a table in the database"""
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS myapp_esg (esg text,environment text,social text,governance text,rank text,
            total text,ricCode text)""")
        print('CREATE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    def store_data(self, item):
        """Store data in the database"""
        self.cur.execute(
            """INSERT INTO myapp_esg (esg,environment,social,governance,rank,total,ricCode)VALUES(?,?,?,?,?,?,?);""",
            (item['esg'], item['environment'], item['social'], item['governance'], item['rank'], item['total'],
             item['ricCode']))
        print('INSERT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        self.cnt.commit()

    def process_item(self, item, spider):
        return super().process_item(item, spider)
