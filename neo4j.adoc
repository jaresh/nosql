= Neo4j 
Jacek Sikora <jaresh@wp.pl>
:icons: font

== Przygotowanie danych

[source, bash]
----
time for i in *.7z; do 7za -y -oextracted x $i; done

Size:       937938638
Compressed: 105420265

real	21m53.298s
user	23m13.552s
sys		0m38.260s

image:/images/neo4j_extract.png[]

*31.6 GB danych
----

Ściągam skrypt do przetwarzenia danych do .csv : 

[source, bash]
----
git clone https://github.com/mdamien/stackoverflow-neo4j

sudo apt-get install python3-setuptools
easy_install3 xmltodict
----

Uruchamiam skrypt:

[source, bash]
----
python3 to_csv.py extracted

real	73m45.879s
user	71m49.554s
sys	0m30.015s

image:/images/neo4j_tocsv.png[]

*4.2 GB danychi
----

Import danych do bazy Neo4j:

[source, bash]
----
./../../Programy/neo4j-community-2.3.0/bin/neo4j-import \
--into ../../Programy/neo4j-community-2.3.0/data/graph.db \
--id-type string \
--nodes:Post "csvs/posts.csv" \
--nodes:User "csvs/users.csv" \
--nodes:Tag "csvs/tags.csv" \
--relationships:PARENT_OF "csvs/posts_rel.csv" \
--relationships:HAS_TAG "csvs/tags_posts_rel.csv" \
--relationships:POSTED "csvs/users_posts_rel.csv"
----

----
TIP: 
Jezeli podczas importu otrzymasz bład dotyczący braku pamieci to należy dodać
do pliku 'neo4j-community-2.3.0/bin/neo4j-import', gdzieś przed wywołaniem 
ostatniego polecenia (wartości -Xms -Xmx zależnie od dostepnej pamięci):

[source, bash]
----
JAVA_OPTS="-Xms2048m -Xmx2048m"
----
----

IMPORT DONE in 26m 41s 500ms. Imported:
  25247894 nodes
  58817742 relationships
  126491554 properties

== Analiza danych

.Ile danych mamy w bazie:
----
neo4j-sh (?)$ match (n) return head(labels(n)) as label, count(*);

image:/images/neo4j_1query.png[]
----

.Dodanie indeksów:

----
create index on :Post(title);
create index on :Post(createdAt);
create index on :Post(score);
create index on :Post(views);
create index on :Post(favorites);
create index on :Post(answers);
create index on :Post(score);

create index on :User(name);
create index on :User(createdAt);
create index on :User(reputation);
create index on :User(age);

create index on :Tag(count);

create constraint on (t:Tag) assert t.tagId is unique;
create constraint on (u:User) assert u.userId is unique;
create constraint on (p:Post) assert p.postId is unique;
----
