"""
This module provides methods to test that the database has been
populated properly.
"""
from db import create_connection


def test_songs():
    """
    Asserts that songs is populated.
    """
    conn = create_connection("sparkifydb")
    cur = conn.cursor()
    query = ("""SELECT COUNT(*) FROM songs;""")
    cur.execute(query)
    result = cur.fetchall()[0][0]
    conn.close()
    assert result > 0

def test_artists():
    """
    Asserts that artists is populated.
    """
    conn = create_connection("sparkifydb")
    cur = conn.cursor()
    query = ("""SELECT COUNT(*) FROM artists;""")
    cur.execute(query)
    result = cur.fetchall()[0][0]
    conn.close()
    assert result > 0

def test_users():
    """
    Asserts that users is populated.
    """
    conn = create_connection("sparkifydb")
    cur = conn.cursor()
    query = ("""SELECT COUNT(*) FROM users;""")
    cur.execute(query)
    result = cur.fetchall()[0][0]
    conn.close()
    assert result > 0

def test_time():
    """
    Asserts that time is populated.
    """
    conn = create_connection("sparkifydb")
    cur = conn.cursor()
    query = ("""SELECT COUNT(*) FROM time;""")
    cur.execute(query)
    result = cur.fetchall()[0][0]
    conn.close()
    assert result > 0

def test_songplays():
    """
    Asserts that songplays is populated.
    """
    conn = create_connection("sparkifydb")
    cur = conn.cursor()
    query = ("""SELECT COUNT(*) FROM songplays;""")
    cur.execute(query)
    result = cur.fetchall()[0][0]
    conn.close()
    assert result > 0


def test_songplays_staging():
    """
    Asserts that songplays_staging is not populated.
    """
    conn = create_connection("sparkifydb")
    cur = conn.cursor()
    query = ("""SELECT COUNT(*) FROM songplays_staging;""")
    cur.execute(query)
    result = cur.fetchall()[0][0]
    conn.close()
    assert result == 0
