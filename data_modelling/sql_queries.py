# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id PRIMARY KEY,
     start_time TIME,
        user_id INTEGER,
          level VARCHAR,
        song_id INTEGER,
      artist_id INTEGER,
     session_id INTEGER,
       location VARCHAR,
     user_agent VARCHAR
);""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
        user_id PRIMARY KEY,
     first_name VARCHAR,
      last_name VARCHAR,
         gender VARCHAR,
          level VARCHAR
);""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
        song_id PRIMARY KEY,
          title VARCHAR,
      artist_id INTEGER,
           year INTEGER,
       duration FLOAT
);""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
      artist_id PRIMARY KEY,
           name VARCHAR,
       location VARCHAR,
      lattitude FLOAT,
      longitude FLOAT
);""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
     start_time DATE,
           hour INTEGER,
            day INTEGER,
           week INTEGER,
          month INTEGER,
           year INTEGER,
        weekday INTEGER
);""")

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