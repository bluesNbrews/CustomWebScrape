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
        restaurants = data.get('explore_tabs')[0].get('sections')[0].get('recommendation_items')
        for restaurant in restaurants:
            yield scrapy.Request(url='https://www.airbnb.com/api/v2/place_activities/{0}?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=USD&locale=en&_format=for_spa_activity_pdp_web'.format(restaurant.get('id')), callback=self.parse)

    def parse(self, response):
        restaurant = json.loads(response.body).get('place_activity')

        yield{
            'id': restaurant.get('id'),
            'title': restaurant.get('title'),
            'type': restaurant.get('action_kicker'),
            'description': restaurant.get('description'),
            'place': {
                'address': restaurant.get('place').get('address'),
                'city': restaurant.get('place').get('city'),
                'country': restaurant.get('place').get('country'),
                'latitude': restaurant.get('place').get('lat'),
                'longitude': restaurant.get('place').get('lng')
            },
            'phone_number': restaurant.get('place').get('phone'),
            'website': restaurant.get('place').get('website')
        }
