## Data Warehouse

Project Data Warehouse as part of the Udactiy Data Engineer Nanodegree.

### Project Summary
An implementation of a Data Warehouse leveraging AWS RedShift.
This projects contains the ETL pipeline:
 - Extracts data from S3
 - Stages the data in Redshift
 - Transforms data into dimension tables for the analytics team.

The S3 data contains song and log information from the music store, and enables music stores to process high volumes of information with efficiency.

### Purpose of this project
This projects processes data from multiple sources. Here have multiple S3 buckets. The processing increases the efficiency of the data analysis of the startup Sparkify's application.

### Instructions
- Setup a redshift cluster on AWS and insert the connection details in dwh.cfg.
- Create the needed the database structure by executing create_tables.py.
- Process the data from the configured S3 data sources by executing etl.py.
#### Database schema
##### Table	Description
staging_events	stating table for event data
staging_songs	staging table for song data
songplays	information how songs were played, e.g. when by which user in which session
users	user-related information such as name, gender and level
songs	song-related information containing name, artist, year and duration
artists	artist name and location (geo-coords and textual location)
time	time-related info for timestamps
ETL pipeline
Load song and log data both from S3 buckets.
Stage the loaded data.
Transform the data into the above described data schema.
Example queries
Find all users at a certain location: SELECT DISTINCT users.user_id FROM users JOIN songplays ON songplays.user_id = users.user_id WHERE songplays.location = <LOCATION>
Find all songs by a given artist: SELECT songs.song_id FROM songs JOIN artists ON songs.artist_id = artists.artist_id WHERE artist.name = <ARTIST>
