import scrapy
from scrapy import FormRequest
from scrapy.spiders import CrawlSpider
from scrapy import Request
from ..items import ScrapItem, EsgItem
from urllib.parse import urljoin
import json


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
            yield Request(f"https://www.refinitiv.com/bin/esg/esgsearchresult?ricCode={item['ricCode']}",
                          callback=self.parse2)
        # print('+' * 1000)

    def parse2(self, response):
        data = EsgItem()
        # print('-' * 1000)
        a = json.loads(response.css('p::text').get())
        esg = a['esgScore']['TR.TRESG']['score']
        environment = a['esgScore']['TR.EnvironmentPillar']['score']
        social = a['esgScore']['TR.SocialPillar']['score']
        governance = a['esgScore']['TR.GovernancePillar']['score']
        rank = a['industryComparison']['rank']
        total = a['industryComparison']['totalIndustries']
        code = response.url[58:]
        data['esg'] = esg
        data['environment'] = environment
        data['social'] = social
        data['governance'] = governance
        data['rank'] = rank
        data['total'] = total
        data['ricCode'] = code
        # print('-' * 1000)
        yield data
