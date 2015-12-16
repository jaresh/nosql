import pymongo
from pymongo import MongoClient
from bson.son import SON

client = MongoClient('localhost', 27017)
db = client.Crimes
collection = db.list

pipeline = [
	{ "$match": {
		"$or":[
			{"Month": "2013-06"},
			{"Month": "2014-06"},
			{"Month": "2015-06"}
		]}	
	},
	{ "$match": {
		"$or":[
			{"Crime type":"Anti-social behaviour"},
			{"Crime type":"Drugs"},
			{"Crime type":"Public order"}
		]}
	},
	{ "$group": {"_id": {"month": "$Month", "crime": "$Crime type"},
 				"total": {"$sum": 1}
				}
	},
	{ "$group": {"_id": "$_id.month",
				"crimes": {"$addToSet": {"crime": "$_id.crime" , "total":"$total"}}
			}
	},
	{ "$sort": SON([("crime", -1)])}
]

result = collection.aggregate(pipeline)

for doc in result:
	print doc
