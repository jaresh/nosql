# Aggregation Pipeline      
####Jacek Sikora 206232 <jaresh@wp.pl>

#Spis treści
- [Przygotowanie danych](#przygotowanie-danych)

# Przygotowanie danych


[Przestępstwa popełnione w Wilekiej Brytani od grudnia 2010 do października 2015.](https://data.police.uk/data/)

5.7 GB

--
Skrypt [imports.sh](scripts/imports.sh) do importu danych z plików .csv:
```bash

#!/bin/bash

files=(`basename -a *`)

for i in ${files[@]}
do
	../../Programy/mongodb-linux-x86_64-3.2.0/bin/mongoimport -d Crimes -c list --type csv --file $i --headerline
done
```
--
Import plików do bazy:
```bash
time ./imports.sh

real	29m52.893s
user	37m30.754s
sys	5m24.873s

```

![mongo](images/importmongo.png)
--
Najważniejsze statystyki bazy:

```js
db.list.stats()
{
	"ns" : "Crimes.list",
	"count" : 29563143,
	"size" : 14698514832,
	"avgObjSize" : 497
}
```

# Agregacje

## Agregacja 1

Najczęstsze przestępstwa w czerwcu 2012 roku:

```js
var connection = new Mongo();
var db = connection.getDB('Crimes');

var match = { $match: {"Month": "2012-6"} };
var group = { $group: {_id: "$Crime type", "total": {$sum: 1}} };
var sort = { $sort: {"total": -1} };
var limit = { $limit : 5};

var results = db.list.aggregate(
	match,
	group,
	sort,
	limit
);

printjson(results);
```
[aggregation1.js](scripts/aggregation1.js)

Wynik
```js
{ "_id" : "Anti-social behaviour", "total" : 204751 }
{ "_id" : "Other theft", "total" : 61978 }
{ "_id" : "Violent crime", "total" : 56816 }
{ "_id" : "Criminal damage and arson", "total" : 44922 }
{ "_id" : "Burglary", "total" : 38791 }

```

| Crime type		| count |
|-------------------|-------|
| Anti-social behaviour		| 204751 |
| Other theft  	| 61978 |
| Violent crime 	| 56816 |
| Criminal damage and arson			| 44922 |
| Burglary 	| 38791 |

![aggr1](images/aggr1.png)

