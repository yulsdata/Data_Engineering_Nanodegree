# DROP TABLES

songplay_table_drop = "DROP table if exists songplays"
user_table_drop = "DROP table if exists users"
song_table_drop = "DROP table if exists songs"
artist_table_drop = "DROP table if exists artists"
time_table_drop = "DROP table if exists time"

# CREATE TABLES

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
                                  user_id int PRIMARY KEY, 
                                  first_name varchar, 
                                  last_name varchar, 
                                  gender varchar, 
                                  level varchar)""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
                                  song_id text PRIMARY KEY, 
                                  title varchar, 
                                  artist_id text NOT NULL, 
                                  year int, 
                                  duration numeric)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
                                    artist_id text PRIMARY KEY, 
                                    name varchar, 
                                    location varchar, 
                                    latitude float, 
                                    longitude float)
""")

time_table_create = (""" 
CREATE TABLE IF NOT EXISTS time (
                                 start_time TIMESTAMP PRIMARY KEY, 
                                 hour int, 
                                 day int, 
                                 week int, 
                                 month int, 
                                 year int, 
                                 weekday int)
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
                                       songplay_id serial PRIMARY KEY, 
                                       start_time time NOT NULL, 
                                       user_id int NOT NULL, 
                                       level varchar, 
                                       song_id text, 
                                       artist_id text, 
                                       session_id int, 
                                       location varchar, 
                                       user_agent varchar)
""")


# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = (""" INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) on conflict (user_id) do nothing
""")

song_table_insert = (""" INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) on conflict (song_id) do nothing
""")

artist_table_insert = (""" INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s) on conflict (artist_id) do nothing
""")


time_table_insert = (""" INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) on conflict (start_time) do nothing
""")

# FIND SONGS

song_select = (""" SELECT a.song_id, 
                         a.artist_id 
                         FROM songs AS a 
                         LEFT JOIN 
                         artists AS b ON a.artist_id = b.artist_id 
                         WHERE a.title=%s AND 
                               b.name=%s AND 
                               a.duration=%s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
