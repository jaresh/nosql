import pymongo
from pymongo import MongoClient
from bson.son import SON

client = MongoClient('localhost', 27017)
db = client.Crimes
collection = db.list

pipeline = [
	{ "$match": {"Month": "2012-06"} }, 
	{ "$group": {"_id": "$Crime type", "total": {"$sum": 1}} }, 
  	{ "$sort": SON([("total", -1)])},
	{ "$limit": 5 }
]

result = collection.aggregate(pipeline)

for doc in result:
	print doc
