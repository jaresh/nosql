import pymongo
from pymongo import MongoClient
from bson.son import SON

client = MongoClient('localhost', 27017)
db = client.Crimes
collection = db.list

pipeline = [
	{ "$match": {
		"$or": [
			{"Reported by": "Sussex Police"},
			{"Reported by": "South Yorkshire Police"},
			{"Reported by": "Metropolitan Police Service"}
		],
		"$and": [
			{"Crime type": "Drugs"}
		]}
	},
	{ "$group": {"_id": "$Reported by", "total": {"$sum": 1}} },
	{ "$sort": SON([("_id", -1)])}
]

result = collection.aggregate(pipeline)

for doc in result:
	print doc
