# -*- coding: utf-8 -*-
import scrapy
import json

class AirbnbSpider(scrapy.Spider):
    name = 'airbnb'
    allowed_domains = ['www.airbnb.com']
    
    def start_requests(self):
        yield scrapy.Request(url='https://www.airbnb.com/api/v2/place_activities/1876?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=USD&locale=en&_format=for_spa_activity_pdp_web', callback = self.parse_id)

    def parse_id(self, response):
        data = json.loads(response.body)
        with open('sample.json', 'w') as file:
            file.write(json.dumps(data))

    def parse(self, response):
        pass
