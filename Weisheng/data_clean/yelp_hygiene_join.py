from pymongo import MongoClient
from yelp.client import Client

client = MongoClient()
db = client.weisheng

counter = 0
yelp_doc_list = db.yelpDataMain.find()
for yelp_doc in yelp_doc_list:
    hygiene_doc = db.hygiene_average.find({'_id.phone':yelp_doc['phone'], '_id.zip_code':yelp_doc['zip_code']})
    if hygiene_doc.count() >= 2:
        for doc in hygiene_doc:
            if yelp_doc['address'].lower().find(doc['_id']['street'].lower()) is True:
                db.yelp_hygiene_join.insert({"display_phone":yelp_doc['display_phone'],
                                             "restaurant_id":yelp_doc['id'],
                                             "name":yelp_doc['name'],
                                             "address":yelp_doc['address'],
                                             "city":yelp_doc['city'],
                                             "latitude":yelp_doc['latitude'],
                                             "longitude":yelp_doc['longitude'],
                                             "zip_code":yelp_doc['zip_code'],
                                             "state":yelp_doc['state'],
                                             "phone":yelp_doc['phone'],
                                             "rating":yelp_doc['rating'],
                                             "hygiene_average_score":doc['value.avg_score']})
                counter += 1
                print(counter)
            else:
                continue
    else:
        for doc in hygiene_doc:
            db.yelp_hygiene_join.insert({"display_phone":yelp_doc['display_phone'],
                                             "restaurant_id":yelp_doc['id'],
                                             "name":yelp_doc['name'],
                                             "address":yelp_doc['address'],
                                             "city":yelp_doc['city'],
                                             "latitude":yelp_doc['latitude'],
                                             "longitude":yelp_doc['longitude'],
                                             "zip_code":yelp_doc['zip_code'],
                                             "state":yelp_doc['state'],
                                             "phone":yelp_doc['phone'],
                                             "rating":yelp_doc['rating'],
                                             "hygiene_average_score":doc['value']['avg_score']})
            counter += 1
            print(counter)

