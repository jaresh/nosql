var connection = new Mongo();
var db = connection.getDB('Crimes');

var result = db.list.aggregate([
	{ $match: {
		$or:[
			{"Month": "2013-06"},
			{"Month": "2014-06"},
			{"Month": "2015-06"}
		]}	
	},
	{ $match: {
		$or:[
			{"Crime type":"Anti-social behaviour"},
			{"Crime type":"Drugs"},
			{"Crime type":"Public order"}
		]}
	},
	{ $group: {_id: {month: "$Month", crime: "$Crime type"},
 				total: {$sum: 1}
				}
	},
	{ $group: {_id: "$_id.month",
				crimes: {$addToSet: {crime: "$_id.crime" , total:"$total"}}
			}
	},
	{ $sort: {crime: -1} }
]);

printjson(result);
