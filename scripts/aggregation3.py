import pymongo
from pymongo import MongoClient
from bson.son import SON

client = MongoClient('localhost', 27017)
db = client.Crimes
collection = db.list

pipeline = [
	{ "$match": {"Month": { "$regex": '2014-[0-9][0-9]', "$options": 'g' }} },
	{ "$match": {
		"$or": [
			{"Crime type":"Anti-social behaviour"},
			{"Crime type":"Other crime"},
			{"Crime type":"Burglary"},
			{"Crime type":"Vehicle crime"},
			{"Crime type":"Robbery"},
			{"Crime type":"Violent crime"},
			{"Crime type":"Other theft"},
			{"Crime type":"Criminal damage and arson"},
			{"Crime type":"Shoplifting"},
			{"Crime type":"Drugs"},
			{"Crime type":"Public disorder and weapons"},
			{"Crime type":"Violence and sexual offences"},
			{"Crime type":"Public order"},
			{"Crime type":"Theft from the person"},
			{"Crime type":"Possession of weapons"},
			{"Crime type":"Bicycle theft"}
		]}
	},
	{ "$group": {"_id": "$Crime type", "total": {"$sum": 1}} }, 
	{ "$sort": SON([("_id", -1)])}
]

result = collection.aggregate(pipeline)

for doc in result:
	print doc
