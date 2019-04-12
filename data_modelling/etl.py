import os
import glob
import psycopg2
import pandas as pd

from data_modelling import sql_queries
from data_modelling.db import create_connection, insert
from data_modelling.etl_steps.prepare import PreparerSongs, PreparerArtists,\
PreparerTime, PreparerUsers, PreparerSongplaysStaging
from data_modelling.etl_steps.read import get_files, read_file


def process_song_file(cur, filepath):
    # create preparers
    preparer_songs = PreparerSongs()
    preparer_artists = PreparerArtists()

    # open song file
    df = read_file(filepath)

    # insert song record
    song_data = preparer_songs.transform(df)
    insert(sql_queries.song_table_insert, song_data, cur)

    # insert artist record
    artist_data = preparer_artists.transform(df)
    insert(sql_queries.artist_table_insert, artist_data, cur)


def process_log_file(cur, filepath):
    # create preparers
    preparer_time = PreparerTime()
    preparer_users = PreparerUsers()
    preparer_songplays_staging = PreparerSongplaysStaging()

    # open log file
    df = read_file(filepath)

    # insert time data
    time_data = preparer_time.transform(df)
    insert(sql_queries.time_table_insert, time_data, cur)

    # insert user data
    user_data = preparer_users.transform(df)
    insert(sql_queries.user_table_insert, user_data, cur)

    # insert songplay staging data
    songplay_staging_data = preparer_songplays_staging.transform(df)
    insert(sql_queries.songplay_staging_table_insert, songplay_staging_data, cur)

    # insert songplay data
    # TODO

    # wipe songplay staging table
    # TODO

def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = get_files(filepath)

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = create_connection("sparkifydb")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
