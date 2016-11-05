from pymongo import MongoClient
from pymongo import *
client = MongoClient('localhost', 27017)
db = client.weisheng
test = {"test":"test"}
collection = db.yelp_join_hygiene.insert(test)
collection = db.yelp_join_hygiene.remove({})




