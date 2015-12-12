#!/bin/bash

files=(`basename -a combined/*`)

echo $files

for i in ${files[@]}
do
	../../Programy/mongodb-linux-x86_64-3.2.0/bin/mongoimport -d Crimes -c list --type csv --file combined/$i --headerline
done
