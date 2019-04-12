# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
songplay_staging_table_drop = "DROP TABLE IF EXISTS songplays_staging;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY,
     start_time BIGINT NOT NULL,
        user_id INTEGER NOT NULL,
          level VARCHAR NOT NULL,
        song_id INTEGER NOT NULL,
      artist_id INTEGER NOT NULL,
     session_id INTEGER NOT NULL,
       location VARCHAR NOT NULL,
     user_agent VARCHAR NOT NULL,
         UNIQUE (start_time,
                user_id)
);""")

songplay_staging_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays_staging (
     start_time BIGINT,
        user_id INT,
          level VARCHAR,
     session_id INT,
       location VARCHAR,
     user_agent VARCHAR,
     song_title VARCHAR,
    artist_name VARCHAR,
  song_duration FLOAT
);""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
     first_name VARCHAR,
      last_name VARCHAR,
         gender VARCHAR,
          level VARCHAR
);""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR PRIMARY KEY,
          title VARCHAR,
      artist_id VARCHAR,
           year INTEGER,
       duration FLOAT
);""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
      artist_id VARCHAR PRIMARY KEY,
           name VARCHAR,
       location VARCHAR,
      lattitude FLOAT,
      longitude FLOAT
);""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
     start_time BIGINT PRIMARY KEY,
           hour INTEGER,
            day INTEGER,
           week INTEGER,
          month INTEGER,
           year INTEGER,
        weekday INTEGER
);""")


# INSERT RECORDS
songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%(start_time)s, %(user_id)s, %(level)s, %(song_id)s, %(artist_id)s, %(session_id)s, %(location)s, %(user_agent)s)
ON CONFLICT DO NOTHING;
""")

songplay_staging_table_insert = ("""
INSERT INTO songplays_staging (start_time, user_id, level, session_id, location, user_agent, song_title, artist_name, song_duration)
VALUES (%(start_time)s, %(user_id)s, %(level)s, %(session_id)s, %(location)s, %(user_agent)s, %(song_title)s, %(artist_name)s, %(song_duration)s)
ON CONFLICT DO NOTHING;
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%(user_id)s, %(first_name)s, %(last_name)s, %(gender)s, %(level)s)
ON CONFLICT DO NOTHING;
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%(song_id)s, %(title)s, %(artist_id)s, %(year)s, %(duration)s)
ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, lattitude, longitude)
VALUES (%(artist_id)s, %(name)s, %(location)s, %(lattitude)s, %(longitude)s)
ON CONFLICT DO NOTHING;
""")

time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%(start_time)s, %(hour)s, %(day)s, %(week)s, %(month)s, %(year)s, %(weekday)s)
ON CONFLICT DO NOTHING;
""")

# FIND SONGS
song_select = ("""
SELECT songs.song_id,
       songs.artist_id
  FROM songs
  LEFT JOIN artists
    ON songs.artist_id = artists.artist_id
 WHERE songs.title = %(title)s
   AND artists.name = %(artist_name)s
   AND duration = %(duration)s;
""")

# WIPE STAGING
songplay_staging_table_wipe = ("""
TRUNCATE IF EXISTS songplays_staging;
""")

# QUERY LISTS
create_table_queries = [songplay_table_create, songplay_staging_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, songplay_staging_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
