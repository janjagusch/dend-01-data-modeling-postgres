"""
This module provides methods to read in the raw data.
"""
import glob
import os

import pandas as pd


def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    return all_files


def read_file(filepath):
    return pd.read_json(filepath, lines=True)
