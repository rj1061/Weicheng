from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['weisheng']
test = {"test":"test"}
db.yelp_join_hygiene.insert(test)
db.yelp_join_hygiene.remove({})
