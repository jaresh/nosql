# Aggregation Pipeline      
####Jacek Sikora 206232 <jaresh@wp.pl>

#Spis treści
- [Przygotowanie danych](#przygotowanie-danych)

# Przygotowanie danych


Przestępstwa popełnione w Wilekiej Brytani od grudnia 2010 do października 2015.

[LINK](https://data.police.uk/data/)

5.7 GB

Skrypt do importu danych z plików .csv:
```bash

#!/bin/bash

files=(`basename -a *`)

for i in ${files[@]}
do
	../../Programy/mongodb-linux-x86_64-3.2.0/bin/mongoimport -d Crimes -c list --type csv --file $i --headerline
done


real	29m52.893s
user	37m30.754s
sys	5m24.873s

```


