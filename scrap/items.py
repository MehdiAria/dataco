# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy_djangoitem import DjangoItem
from myapp.models import Company


class ScrapItem(DjangoItem):
    """ItemAdapter for scrapy"""
    django_model = Company
