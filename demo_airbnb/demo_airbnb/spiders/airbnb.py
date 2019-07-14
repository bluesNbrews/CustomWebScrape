# -*- coding: utf-8 -*-
import scrapy
import json

class AirbnbSpider(scrapy.Spider):
    name = 'airbnb'
    allowed_domains = ['www.airbnb.com']
    
    def start_requests(self):
        #yield scrapy.Request(url='https://www.airbnb.com/api/v2/explore_tabs?version=1.3.9&satori_version=1.0.7&_format=for_explore_search_web&experiences_per_grid=20&items_per_grid=18&guidebooks_per_grid=20&auto_ib=false&fetch_filters=true&has_zero_guest_treatment=false&is_guided_search=true&is_new_cards_experiment=true&luxury_pre_launch=false&query_understanding_enabled=true&show_groupings=true&supports_for_you_v3=true&timezone_offset=120&client_session_id=e44973e0-2a63-4e3d-9e9c-75e7708f5f3a&metadata_only=false&is_standard_search=true&refinement_paths%5B%5D=%2Frestaurant&selected_tab_id=restaurant_tab&adults=1&children=0&infants=0&guests=1&screen_size=large&query=New%20York&_intents=p1&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=USD&locale=en', callback = self.parse_id)
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
