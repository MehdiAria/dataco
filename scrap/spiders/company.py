import scrapy
from ..items import ScrapItem


class EsgSpider(scrapy.Spider):
    """Spider to crawl companyName data"""
    name = 'esg'
    allowed_domains = ['www.refinitiv.com']
    start_urls = ['https://www.refinitiv.com/bin/esg/esgsearchsuggestions']

    def parse(self, response, **kwargs):
        data = ScrapItem()
        items = response.json()
        for item in items:
            data['companyName'] = item['companyName']
            data['ricCode'] = item['ricCode']
            yield data
