# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay_table"
user_table_drop = "DROP TABLE IF EXISTS user_table_drop"
song_table_drop = "DROP TABLE IF EXISTS song_table_drop"
artist_table_drop = "DROP TABLE IF EXISTS artist_table_drop"
time_table_drop = "DROP TABLE IF EXISTS time_table_drop"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
songplay_id SERIAL PRIMARY KEY, 
start_time varchar, 
user_id int, 
level varchar, 
song_id varchar, 
artist_id varchar, 
session_id varchar, 
location text, 
user_agent text
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
user_id int PRIMARY KEY, 
first_name varchar NOT NULL, 
last_name varchar NOT NULL, 
gender varchar, 
level varchar
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
song_id varchar PRIMARY KEY, 
title varchar NOT NULL, 
artist_id varchar, 
year int, duration float
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
artist_id varchar PRIMARY KEY, 
name varchar NOT NULL, 
location text, 
latitude float, 
longitude float
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
start_time int PRIMARY KEY NOT NULL, 
hour int, 
day int, 
week int, 
month int, 
year int, 
weekday int
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]