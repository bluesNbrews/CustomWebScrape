# -*- coding: utf-8 -*-
import scrapy


class AirbnbSpider(scrapy.Spider):
    name = 'airbnb'
    allowed_domains = ['www.airbnb.com']
    start_urls = ['http://www.airbnb.com/']

    def parse(self, response):
        pass
