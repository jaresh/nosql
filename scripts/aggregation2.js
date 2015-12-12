var connection = new Mongo();
var db = connection.getDB('Crimes');

var result = db.list.aggregate([
	{ $match: {"Reported by": "Avon and Somerset Constabulary"} },
	{ $match: {"Crime type": "Burglary"} },
	{ $group: {_id: "$Month", "total": {$sum: 1}} }, 
	{ $sort: {"_id": -1} }
]);

printjson(result);
