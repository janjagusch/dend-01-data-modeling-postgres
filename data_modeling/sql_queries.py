"""
This module provides sql queries for creating,
inserting into and dropping tables.
"""
# DROP TABLES
SONGPLAY_TABLE_DROP = "DROP TABLE IF EXISTS songplays;"
SONGPLAY_STAGING_TABLE_DROP = "DROP TABLE IF EXISTS songplays_staging;"
USER_TABLE_DROP = "DROP TABLE IF EXISTS users;"
SONG_TABLE_DROP = "DROP TABLE IF EXISTS songs;"
ARTIST_TABLE_DROP = "DROP TABLE IF EXISTS artists;"
TIME_TABLE_DROP = "DROP TABLE IF EXISTS time;"

# CREATE TABLES#
SONGPLAY_TABLE_CREATE = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY,
     start_time BIGINT NOT NULL REFERENCES time(start_time) ON DELETE RESTRICT,
        user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE RESTRICT,
          level VARCHAR NOT NULL,
        song_id VARCHAR NOT NULL REFERENCES songs(song_id) ON DELETE RESTRICT,
      artist_id VARCHAR NOT NULL REFERENCES artists(artist_id) ON DELETE RESTRICT,
     session_id INTEGER NOT NULL,
       location VARCHAR NOT NULL,
     user_agent VARCHAR NOT NULL,
         UNIQUE (start_time, user_id, song_id, artist_id)
);""")

SONGPLAY_STAGING_TABLE_CREATE = ("""
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

USER_TABLE_CREATE = ("""
CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
     first_name VARCHAR,
      last_name VARCHAR,
         gender VARCHAR,
          level VARCHAR
);""")

SONG_TABLE_CREATE = ("""
CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR PRIMARY KEY,
          title VARCHAR,
      artist_id VARCHAR,
           year INTEGER,
       duration FLOAT
);""")

ARTIST_TABLE_CREATE = ("""
CREATE TABLE IF NOT EXISTS artists (
      artist_id VARCHAR PRIMARY KEY,
           name VARCHAR,
       location VARCHAR,
      lattitude FLOAT,
      longitude FLOAT
);""")

TIME_TABLE_CREATE = ("""
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
SONGPLAY_TABLE_INSERT = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%(start_time)s, %(user_id)s, %(level)s, %(song_id)s, %(artist_id)s, %(session_id)s, %(location)s, %(user_agent)s)
ON CONFLICT DO NOTHING;
""")

SONGPLAY_STAGING_TABLE_INSERT = ("""
INSERT INTO songplays_staging (start_time, user_id, level, session_id, location, user_agent, song_title, artist_name, song_duration)
VALUES (%(start_time)s, %(user_id)s, %(level)s, %(session_id)s, %(location)s, %(user_agent)s, %(song_title)s, %(artist_name)s, %(song_duration)s)
ON CONFLICT DO NOTHING;
""")

USER_TABLE_INSERT = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%(user_id)s, %(first_name)s, %(last_name)s, %(gender)s, %(level)s)
ON CONFLICT DO NOTHING;
""")

SONG_TABLE_INSERT = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%(song_id)s, %(title)s, %(artist_id)s, %(year)s, %(duration)s)
ON CONFLICT DO NOTHING;
""")

ARTIST_TABLE_INSERT = ("""
INSERT INTO artists (artist_id, name, location, lattitude, longitude)
VALUES (%(artist_id)s, %(name)s, %(location)s, %(lattitude)s, %(longitude)s)
ON CONFLICT DO NOTHING;
""")

TIME_TABLE_INSERT = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%(start_time)s, %(hour)s, %(day)s, %(week)s, %(month)s, %(year)s, %(weekday)s)
ON CONFLICT DO NOTHING;
""")

# MIGRATE STAGING
SONGPLAY_STAGING_TABLE_MIGRATE = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
SELECT songplays_staging.start_time,
       songplays_staging.user_id,
       songplays_staging.level,
       songs_artists.song_id,
       songs_artists.artist_id,
       songplays_staging.session_id,
       songplays_staging.location,
       songplays_staging.user_agent
  FROM songplays_staging
  LEFT JOIN (
       SELECT songs.song_id,
              artists.artist_id,
              songs.title,
              artists.name,
              songs.duration
         FROM songs
         LEFT JOIN artists
           ON songs.artist_id = artists.artist_id)
    AS songs_artists
    ON songplays_staging.song_title = songs_artists.title
   AND songplays_staging.artist_name = songs_artists.name
   AND songplays_staging.song_duration = songs_artists.duration
WHERE songs_artists.song_id IS NOT NULL
ON CONFLICT DO NOTHING;
""")

# WIPE STAGING
SONGPLAY_STAGING_TABLE_WIPE = ("""
TRUNCATE songplays_staging;
""")

# QUERY LISTS
CREATE_TABLE_QUERIES = [USER_TABLE_CREATE, SONG_TABLE_CREATE,
                        ARTIST_TABLE_CREATE, TIME_TABLE_CREATE,
                        SONGPLAY_TABLE_CREATE, SONGPLAY_STAGING_TABLE_CREATE]

DROP_TABLE_QUERIES = [USER_TABLE_DROP, SONG_TABLE_DROP, ARTIST_TABLE_DROP,
                      TIME_TABLE_DROP, SONGPLAY_TABLE_DROP,
                      SONGPLAY_STAGING_TABLE_DROP]
