import json
from pymongo import MongoClient

from streamparse import Bolt


class YelpDataMainBolt(Bolt):

    def process(self, tup):
        jsonFiles = tup.values[0]
        try:
            dictData = json.loads(jsonFiles)
        except ValueError:
            self.logger.info('Empty JSON or bad Response ' + jsonFiles)
        else:
            client = MongoClient('mongodb://localhost:27017/')
            db = client['weisheng']

            for business in dictData['businesses']:
                db['yelpDataMain'].insert(business)
            db.close
