from pymongo import MongoClient
from streamparse import Spout
import json

class readHygiene(Spout):
    outputs = ['hygiene_record']

    def initialize(self, storm_conf, context):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['weisheng']
        self.aggregatedCollection = 'hygiene'
        self.counter = 0
        self.total = self.db[self.aggregatedCollection].find().count()

    def _increment(self):
        if self.counter>self.total:
            self.counter = 0
        self.counter += 1

    def fail(self, tup_id):
        self.logger.error("Error: "+tup_id)

    def next_tuple(self):
        self.logger.info(str(self.counter))
        if(self.counter<self.total):
            self.rec = self.db[self.aggregatedCollection].find({}, {"_id": 0})[self.counter]
            self._increment()
        try:
            self.recordJson = json.dumps(self.rec)
        except ValueError:
            self.logger.error("Value Error while dumping "+str(self.rec)+" into a JSON")
        else:
            #self.logger.info("Response: " + self.recordJson)
            self.emit([self.recordJson])