var connection = new Mongo();
var db = connection.getDB('Crimes');

var result = db.list.aggregate([
	{ $match: {"Month": "2012-06"} }, 
	{ $group: {_id: "$Crime type", "total": {$sum: 1}} }, 
	{ $sort: {"total": -1} }, { $limit : 5}
]);

printjson(result);
