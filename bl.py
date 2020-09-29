import json

from pymongo import MongoClient

client = MongoClient()
db = client.metaapi
collection = db.apis

def store_endpoint(data):
    return collection.insert_one(data).inserted_id


def get_all():
    result = ""
    for doc in collection.find():
        id = str(doc['_id'])
        doc["_id"] = id
        result += json.dumps(doc) + "\n"

    return result