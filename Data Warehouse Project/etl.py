import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """ 
    populates the staging tables (staging_events and staging_songs) using data from S3
    
    the COPY command is employed here     
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """ 
    populates the final tables with data from the staging tables (staging_events and taging_songs)
    
    INSERT INTO from a query is employed here.
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """ 
    parses and reads the content of dwh.cfg
    
    creates connection with redshift and cursor
    
    populates the staging tables (staging_events and staging_songs)
    
    populates the final tables with data from the staging tables
    
    terminates the connection with redshift
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    """
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(config.get("DWH","HOST"), 
                                                                                   config.get("DWH","DB_NAME"),
                                                                                   config.get("DWH","DB_USER"),
                                                                                   config.get("DWH","DB_PASSWORD"),
                                                                                   config.get("DWH","DB_PORT")))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
