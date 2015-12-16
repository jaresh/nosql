import pymongo
from pymongo import MongoClient
from bson.son import SON

client = MongoClient('localhost', 27017)
db = client.Crimes
collection = db.list

pipeline = [
	{ "$match": {"Reported by": "Avon and Somerset Constabulary"} },
	{ "$match": {"Crime type": "Burglary"} },
	{ "$group": {"_id": "$Month", "total": {"$sum": 1}} }, 
	{ "$sort": SON([("_id", -1)])}
]

result = collection.aggregate(pipeline)

for doc in result:
	print doc
