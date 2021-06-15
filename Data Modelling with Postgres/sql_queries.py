# DROP TABLES

songplay_table_drop = "DROP table if exists songplays"
user_table_drop = "DROP table if exists users"
song_table_drop = "DROP table if exists songs"
artist_table_drop = "DROP table if exists artists"
time_table_drop = "DROP table if exists time"

# CREATE TABLES

songplay_table_create = (""" 
CREATE TABLE IF NOT EXISTS songplays (songplay_id serial PRIMARY KEY, start_time time, user_id int, level text, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar)
""")

user_table_create = (""" 
CREATE TABLE IF NOT EXISTS users (user_id int, first_name text, last_name text, gender text, level text)
""")

song_table_create = (""" 
CREATE TABLE IF NOT EXISTS songs (
                                  song_id varchar, 
                                  title varchar, 
                                  artist_id varchar, 
                                  year int, 
                                  duration FLOAT)
""")

artist_table_create = (""" 
CREATE TABLE IF NOT EXISTS artists (
                                    artist_id varchar, 
                                    name text, 
                                    location varchar, 
                                    latitude varchar, 
                                    longitude varchar)
""")

time_table_create = (""" 
CREATE TABLE IF NOT EXISTS time (start_time time, hour int, day int, week int, month int, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = (""" INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = (""" INSERT INTO songs (song_id, 
                                            title, 
                                            artist_id, 
                                            year, 
                                            duration) 
                                            VALUES (%s, %s, %s, %s, %s)
                                            on conflict (song_id) do nothing
""")

artist_table_insert = (""" INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = (""" INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
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
