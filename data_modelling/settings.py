"""
This module provides access to the dotenv settings.
"""
import os
from os.path import join, dirname

from dotenv import load_dotenv


DOTENV_PATH = join(dirname(__file__), '.env')
load_dotenv(DOTENV_PATH)

DB_USER_NAME = os.environ.get("DB_USER_NAME")
DB_USER_PASSWORD = os.environ.get("DB_USER_PASSWORD")
