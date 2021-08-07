import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""
create table if not exists staging_events (
                                            event_id        INT IDENTINY(0,1),
                                            artist          VARCHAR,
                                            auth            VARCHAR,
                                            firstName       VARCHAR,
                                            gender          VARCHAR,
                                            iteminSession   VARCHAR,
                                            lastName        VARCHAR,
                                            length          VARCHAR,
                                            level           VARCHAR,
                                            location        VARCHAR,
                                            method          VARCHAR,
                                            page            VARCHAR,
                                            registration    VARCHAR,
                                            sessionid       INT SORTKEY DISTKEY,
                                            song            VARCHAR,
                                            status          INT,
                                            ts              INT,
                                            userAgent       VARCHAR,
                                            userid          VARCHAR
                                            )

""")

staging_songs_table_create = ("""
create table if not exists staging_songs (
                                          song_id             VARCHAR,
                                          num_songs           INT,
                                          artist_id           VARCHAR SORTKEY DISTKEY,
                                          artist_latitude     VARCHAR,
                                          artist_longitude    VARCHAR,
                                          artist_location     VARCHAR,
                                          artist_name         VARCHAR,
                                          duration            NUMERIC,
                                          year                INT
                                          )

""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
                                      songplay_id   INT IDENTITY(0,1)  NOT NULL  SORTKEY, 
                                      start_time    timestamp  NOT NULL,
                                      user_id       INT        NOT NULL    DISTKEY, 
                                      level         text       NOT NULL, 
                                      song_id       VARCHAR    NOT NULL, 
                                      artist_id     VARCHAR    NOT NULL, 
                                      session_id    INT        NOT NULL, 
                                      location      VARCHAR    NULL, 
                                      user_agent    VARCHAR    NULL
                                      )
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
                                    user_id        INT       NOT NULL    SORTKEY, 
                                    first_name     VARCHAR   NULL, 
                                    last_name      VARCHAR   NULL,
                                    gender         VARCHAR   NULL, 
                                    level          varchar   NULL
                                    )
                                    diststyle all
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
                                  song_id    VARCHAR   NOT NULL   SORTKEY,
                                  title      VARCHAR   NOT NULL,
                                  artist_id  VARCHAR   NOT NULL,
                                  year       INT       NOT NULL, 
                                  duration   FLOAT     NOT NULL
                                  )
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
                                    artist_id    VARCHAR   NOT NULL   SORTKEY,
                                    name         VARCHAR   NULL,
                                    location     VARCHAR   NULL,
                                    latitude     NUMERIC   NULL,
                                    longitude    NUMERIC   NULL
                                    )
                                    diststyle all
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
                                  start_time  TIMESTAMP   NOT NULL SORTKEY,
                                  hour        INT         NULL,
                                  day         INT         NULL,
                                  week        INT         NULL,
                                  month       INT         NULL,
                                  year        INT         NULL,
                                  weekday     INT         NULL
                                  ) 
                                  diststyle all
""")

# STAGING TABLES

staging_events_copy = ("""
COPY staging_events FROM {}
     credentials 'aws_iam_role={}'
    format as json {}
    STATUPDATE ON
    region 'us-west-2';
""").format(config.get('S3', 'LOG_DATA'), config.get('IAM_ROLE', 'ARN'), config.get('S3', 'LOG_JSONPATH'))

staging_songs_copy = ("""
    COPY staging_songs FROM {}
    credentials 'aws_iam_role={}'
    format as json 'auto'
    ACCEPTINVCHARS AS '^'
    STATUPDATE ON
    region 'us-west-2';
""").format(config.get('S3', 'SONG_DATA'), config.get('IAM_ROLE', 'ARN'))

# FINAL TABLES

songplay_table_insert = ("""
    INSERT INTO songplays (
        start_time,
        user_id,
        level,
        song_id,
        artist_id,
        session_id,
        location,
        user_agent)
    SELECT  DISTINCT TIMESTAMP 'epoch' + se.ts/1000 * INTERVAL '1 second'   AS start_time,
            sp.userId,
            sp.level,
            ss.song_id,
            ss.artist_id,
            sp.sessionId,
            sp.location,
            sp.userAgent
    FROM songplays AS sp
    JOIN staging_songs AS ss ON (ss.title =sp.song AND ss.artist_name = sp.artist)
    WHERE sp.page = 'NextSong'
""")

user_table_insert = ("""
    INSERT INTO users (
        user_id,
        first_name,
        last_name,
        gender,
        level)
    SELECT  DISTINCT userId,
            firstName,
            lastName,
            gender,
            level
    FROM songplays
    WHERE page = 'NextSong'
""")

song_table_insert = ("""
    INSERT INTO songs (
        song_id,
        title,
        artist_id,
        year,
        duration)
    SELECT  DISTINCT song_id,
            title,
            artist_id,
            year,
            duration
    FROM staging_songs
""")

artist_table_insert = ("""
    INSERT INTO artists (
        artist_id,
        name,
        location,
        latitude,
        longitude)
    SELECT  DISTINCT artist_id,
        artist_name,
        artist_location,
        artist_latitude,
        artist_longitude
    FROM staging_songs
""")

time_table_insert = ("""
    INSERT INTO time (                  
        start_time,
        hour,
        day,
        week,
        month,
        year,
        weekday)
    SELECT  DISTINCT TIMESTAMP 'epoch' + ts/1000 * INTERVAL '1 second'  AS start_time,
            EXTRACT(hour FROM start_time)    AS hour,
            EXTRACT(day FROM start_time)     AS day,
            EXTRACT(week FROM start_time)    AS week,
            EXTRACT(month FROM start_time)   AS month,
            EXTRACT(year FROM start_time)    AS year,
            EXTRACT(week FROM start_time)    AS weekday
    FROM    songplays
    WHERE page = 'NextSong'
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
