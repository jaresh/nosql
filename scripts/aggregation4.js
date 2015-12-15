var connection = new Mongo();
var db = connection.getDB('Crimes');

var result = db.list.aggregate([
	{ $match: {
		$or: [
			{"Reported by": "Sussex Police"},
			{"Reported by": "South Yorkshire Police"},
			{"Reported by": "Metropolitan Police Service"}
		],
		$and: [
			{"Crime type": "Drugs"}
		]}
	},
	{ $group: {_id: "$Reported by", "total": {$sum: 1}} },
	{ $sort: {"_id": -1} }
]);

printjson(result);
