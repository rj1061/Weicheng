import os
import json
from pymongo import MongoClient
from collections import Counter

from streamparse import Bolt


class WordCountBolt(Bolt):
    outputs = ['word', 'count']

    def initialize(self, conf, ctx):
        self.counter = Counter()
        self.pid = os.getpid()
        self.total = 0

    def process(self, tup):
        jsonFiles = tup.values[0];
        client = MongoClient('mongodb://localhost:27017/')
        db = client['weisheng']

        counter = 0
        #    for jsonFile in jsonFiles:
        with open(jsonFiles, 'r') as f:
            for line in f:
                # load valid lines (should probably use rstrip)
                if len(line) < 10: continue
                db['yelpDataMain'].insert(json.load(line))
                counter += 1
                print "loaded line: ", counter
        f.close
        db.close

        if 0 == counter:
            print "Warning: No Records were Loaded"
        else:
            print "loaded a total of ", counter, " lines"
