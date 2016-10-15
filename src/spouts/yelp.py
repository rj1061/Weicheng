from streamparse import Spout
import json
import random

import requests

class YelpSpout(Spout):
    outputs = ['searchJson']

    def initialize(self, stormconf, context):
        self.min_lat = 40512731
        self.max_lat = 40934936
        self.max_long = 74241565
        self.min_long = 73738435

    def next_tuple(self):
        r = requests.post('https://api.yelp.com/oauth2/token', data = {'client_id': 'TT0MY1xkJnhPHM78StQsTw',
                                                                       'client_secret': 'rE7bOW2mX1Llg1CmX6ZL4PGe21mpOBlXjxSa1m1xx3h8KB1MyZ11yShThqnoK9dP'})

        self.lat = round(float((self.min_lat + random.randint(0, self.max_lat - self.min_lat)))/1000000, 6)
        self.long = round(float((self.min_long + random.randint(0, self.max_long - self.min_long)))/-1000000, 6)
        self.logger.info("Latitude: " + str(self.lat)+ " Longitude: " + str(self.long))

        self.logger.info("Log: " + r.content)

        self.access_json = json.loads(r.text)
        self.token = self.access_json['access_token']
        self.searchJson = requests.request('GET',
                                           'https://api.yelp.com/v3/businesses/search',
                                           params = {'latitude': str(self.lat),
                                                     'longitude': str(self.long),
                                                     'limit': '50',
                                                     'term': 'restaurants'},
                                           headers = {'Authorization': 'Bearer ' + self.token})

        self.logger.info("Response: " + self.searchJson.content)

        self.emit([self.searchJson.content])