from pymongo import MongoClient
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key="WsiK54vN1d2p83KimpduGA",
    consumer_secret="Tk3ngkKTjSUJox4mXRFg7UNo2Kc",
    token="q8ngN6oDWaaJ0Mv893BVX2pBv8cU-Q7b",
    token_secret="AohTphxB-gszFtkObrD1gCuIzR8"
)
Mclient = MongoClient()
client = Client(auth)

db = Mclient.weisheng
phoneNumber_list = db.hygiene.distinct('PHONE')

for ph in phoneNumber_list:
    print(ph)
    try:
        result_list = client.phone_search(phone=ph)
        for result in result_list.businesses:
            print(result.id)
            db.YelpDataMain.insert({'id':result.id, 'name':result.name, 'phone':result.phone, 'rating':result.rating,'city':result.location.city,'address':result.location.address})
    except:
        continue;
