from psycopg2.errors import UniqueViolation, NotNullViolation
from sqlalchemy import create_engine as _create_engine
import psycopg2

from data_modelling import settings


def create_connection(database, user_name=None, user_password=None,
                      host="127.0.0.1", port=5432, connection_string=None):
    if connection_string is not None:
        return _create_engine(connection_string)
    if user_name is None:
        user_name = settings.DB_USER_NAME
    if user_password is None:
        user_password = settings.DB_USER_PASSWORD
    connection_dict = {
        "host": host,
        "user_name": user_name,
        "user_password": user_password,
        "database": database
    }
    return psycopg2.connect(
        "host={host} dbname={database} \
        user={user_name} password={user_password}".format(**connection_dict))


def insert(query, records, cur):
    for record in records:
        success = True
        cur.execute(query, record)
        # try:
        #     cur.execute(query, record)
        # except UniqueViolation:
        #     print("Record violates UNIQUE constraint.")
        #     success = False
        # except NotNullViolation:
        #     print("Record violates NOT NULL constraint.")
        #     success = False
        # except Exception as error:
        #     print("An unkown error has occured.")
        #     print(error)
        #     success = False
        # if success:
        #     print("Record inserted successfully.")
