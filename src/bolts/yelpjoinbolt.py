from streamparse import Bolt
from pymongo import MongoClient

import requests
import json

class YelpJoinBolt(Bolt):

    def process(self, tup):
        try:
            self.dataJson = json.loads(tup.values[0])
        except:
            self.logger.error("Error: Loading Json: " + tup.values[0])
        else:
            r = requests.post('https://api.yelp.com/oauth2/token',
                              data = {'client_id': 'TT0MY1xkJnhPHM78StQsTw',
                                      'client_secret': 'rE7bOW2mX1Llg1CmX6ZL4PGe21mpOBlXjxSa1m1xx3h8KB1MyZ11yShThqnoK9dP'})
            try:
                self.access_json = json.loads(r.text)
                self.token = self.access_json['access_token']

                if 'PHONE' in self.dataJson.keys():
                    self.phone = self.dataJson['PHONE']
                    self.phoneSearchJson = requests.request('GET',
                                                            'https://api.yelp.com/v3/businesses/search/phone',
                                                            params = {'phone':str(self.phone)},
                                                            headers = {'Authorization': 'Bearer ' + self.token})
                    if 'error' in json.loads(self.phoneSearchJson.content):
                        self.name = self.dataJson['DBA']
                        self.street = self.dataJson['STREET']
                        self.nameSearchJson = requests.request('GET',
                                                               'https://api.yelp.com/v3/businesses/search',
                                                               params={'term': str(self.name),
                                                                       'location': str(self.street)},
                                                               headers={'Authorization': 'Bearer ' + self.token})
                        self.nameJsonDump = json.loads(self.nameSearchJson.content)
                        if 'total' in self.nameJsonDump and self.nameJsonDump['total'] > 0:
                            self.final = {key: value for (key, value) in (self.nameJsonDump['businesses'][0].items() + self.dataJson.items())}
                            self.logger.info(self.final)
                            client = MongoClient('mongodb://localhost:27017/')
                            db = client['weisheng']
                            db['yelpDataMain'].insert(self.final)
                            db.close
                        else:
                            self.logger.info("Nothing Returned for " + self.name + " " + self.street)
                else:
                    self.logger.info("Error: Nothing to search for " + self.dataJson)
            except:
                self.logger.info("Error: No Json decoded " + self.dataJson)
