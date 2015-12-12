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

[JavaScript](scripts/aggregation1.js)
```js
var connection = new Mongo();
var db = connection.getDB('Crimes');

var result = db.list.aggregate([
	{ $match: {"Month": "2012-06"} }, 
	{ $group: {_id: "$Crime type", "total": {$sum: 1}} }, 
	{ $sort: {"total": -1} }, { $limit : 5}
]);

printjson(result);

```

| Crime type		| count |
|-------------------|-------|
| Anti-social behaviour		| 204751 |
| Other theft  	| 61978 |
| Violent crime 	| 56816 |
| Criminal damage and arson			| 44922 |
| Burglary 	| 38791 |

![aggr1](images/aggr1.png)

--

## Agregacja 2

Krzywa ilości dokonanych włamań zgłoszonych przez Avon and Somerset Constabulary w latach 2010-2015:

[JavaScript](scripts/aggregation2.js)
```js
var connection = new Mongo();
var db = connection.getDB('Crimes');

var result = db.list.aggregate([
	{ $match: {"Reported by": "Avon and Somerset Constabulary"} },
	{ $match: {"Crime type": "Burglary"} },
	{ $group: {_id: "$Month", "total": {$sum: 1}} }, 
	{ $sort: {"_id": -1} }
]);

printjson(result);

```

Wynik

![aggr2](images/aggr2.png)


