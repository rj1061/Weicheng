import json
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
total = len(phoneNumber_list)
cursor = 1

file = open('yelpDataMain.json','a')

for ph in phoneNumber_list:
    print(ph)
    cursor = cursor + 1
    try:
        result_list = client.phone_search(phone=ph)
        for result in result_list.businesses:
            print(result.id)
            document = {"display_phone":result.display_phone,
                        "id":result.id,
                        "name":result.name,
                        "address":result.location.address[0],
                        "city":result.location.city,
                        "latitude":result.location.coordinate.latitude,
                        "longitude":result.location.coordinate.longitude,
                        "zip_code":result.location.postal_code,
                        "state":result.location.state_code,
                        "phone":result.phone,
                        "rating":result.rating}
            try:
                j = json.dumps(document)
            except:
                print("Something wrong with json dump")

            try:
                file.write(j+"\n")
                #if cursor != total:
                    #file.write("")
            except:
                print("Something wrong with file write")

    except:
        continue;

file.close()
