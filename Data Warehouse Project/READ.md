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
- Staging_events	stating table for event data
- Staging_songs	staging table for song data
- Songplays	information how songs were played, e.g. when by which user in which session
- Users	user-related information such as name, gender and level
- Songs	song-related information containing name, artist, year and duration
- Artists	artist name and location (geo-coords and textual location)
- time	time-related info for timestamps

#### ETL pipeline
- Load song and log data both from S3 buckets.
- Stage the loaded data.
- Transform the data into the above described data schema.

### How to Run
1. Create tables by running 'create_tables.py'.
2. Execute ETL process by running 'etl.py'.
