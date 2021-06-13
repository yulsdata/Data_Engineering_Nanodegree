# Project Overview

Sparkify would like to analyse data they are collecting from their music streaming app. The analytics team in interested in understanding what songs are being listened to. The data is stored in directories for JSON logs for user activity and JSON metadata of all the songs. They would like the data in a Postgres database via an ETL process to enable analysis.

## Data
Data is stored of JSON files under two folders
- Songs
    - metadata about songs
- Logs
    - user activity

## Database Components
For analysis a Star Schema data model was developed containing a fact table and four dimension tables.

Fact table
- *songplays* stores the song play records, containing info for each song play
Dimension tables
- *songs* stores the songs in the music database
- *artists* stores the artists the in music database
- *users* stores the users in the app
- *time* stores the timestamps of records in songplays by specific units


## ETL
An ETL to extract data from the source and upload into *Postgres* was created.

The ETL contains the following:
1. sql_queries.py
    - contains the sql queries used by the *create_tables.py* and *etl.py* python programs.
2. create_tables.py
    - drops and creates database and tables
3. etl.py
    - accesses, transforms and pushes data to the various postgres tables

There are two additional files (jupyter notebooks) used to prototype and test the ETL application.
4. etl.ipynb
5. test.ipynb

The ETL program uses the following file path structure:
/data/song_data/ <subfolders> / <files>
/data/log_data/  <subfolders> / <files>   


## How it works
1. On your terminal, run create_tables.py  -  This will drop the tables if they already exist and create new ones.
    python create_tables.py
2. run etl.py  -  This will extract the data from JSON files and insert them into respective tables.
    python etl.py