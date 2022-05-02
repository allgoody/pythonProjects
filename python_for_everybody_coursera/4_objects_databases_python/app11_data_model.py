# JOIN operation links across several tables as part of SELECT

# Don't put same string data in twice - use relationship instead

# Primary key - particular row / unique number

# Eg: album's primary key ends up being Track's foreing key ( bc the track belongs to the album)

# Make senseble name - eg:
# album's primary key ID ( id ) could be in Track's foreing key ID ( album_id )

# Logical key -  unique id to get item from outside

# Table - Primary key - Logical key - Foreing key

# Creating table in DB start from the TOP to be able to use their ids as Foreing keys

# CREATE TABLE Album (
# 	id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     artist_id INTEGER,
# 	title  TEXT
# )

# CREATE TABLE Genre(
# 	id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
# 	name  TEXT
# )


# CREATE TABLE Track (
# 	id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     album_id INTEGER,
#     genre_id INTEGER,
# 	title  TEXT,
# 	len INTEGER,
# 	rating INTEGER,
# 	count INTEGER
# );


# insert into Artist (name) values ('Led Zepplin');
# insert into Artist (name) values ('AC/DC')

# insert into Album (title,artist_id) values ('Who Made Who',2);
# insert into Album (title,artist_id) values ('IV',1)

# insert into Track (title,rating,len,count,album_id,genre_id) values ('Black Dog',5,297,0,2,1);
# insert into Track (title,rating,len,count,album_id,genre_id) values ('Stairway',5,482,0,2,1);
# insert into Track (title,rating,len,count,album_id,genre_id) values ('About to Rock',5,313,0,1,2);
# insert into Track (title,rating,len,count,album_id,genre_id) values ('Who Made Who',5,207,0,1,2)

# eg of join:
#
# SELECT Album.title,Artist.name FROM Album JOIN Artist ON Album.artist_id = Artist.id

# JOIN ON
# SELECT Album.title, Album.artist_id,Artist.id,Artist.name FROM Album JOIN Artist ON Album.artist_id = Artist.id
# WHERE
# SELECT Album.title, Album.artist_id,Artist.id,Artist.name FROM Album, Artist WHERE Album.artist_id = Artist.id

# SELECT Track.title, Genre.name FROM Track JOIN Genre ON Track.genre_id = Genre.id

# SELECT Track.title, Artist.name,Album.title,Genre.name
#  FROM
#  Track
#  JOIN Genre
#  JOIN Album
#  JOIN Artist
#  ON
#  Track.genre_id = Genre.id
#  AND Track.album_id = Album.id
#  AND Album.artist_id = Artist.id