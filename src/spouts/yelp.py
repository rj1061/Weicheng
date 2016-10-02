from streamparse import Spout

import requests

class YelpSpout(Spout):
    outputs = ['something']

    def initialize(self, stormconf, context):

        self.thing = "something"

    def next_tuple(self):
        r = requests.post('https://api.yelp.com/oauth2/token', data={'client_id': 'TT0MY1xkJnhPHM78StQsTw',
                                                                    'client_secret': 'rE7bOW2mX1Llg1CmX6ZL4PGe21mpOBlXjxSa1m1xx3h8KB1MyZ11yShThqnoK9dP'})
        self.logger.info("Log: " + r.text)
        self.emit(['something'])