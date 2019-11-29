# !/Users/kbsriharsha/anaconda3/bin/python
# coding: utf-8
# @author: Bharat Sri Harsha karpurapu
"""
This program provides the functions for the database operations
"""

# Importing libraries
import sqlite3
from sqlite3 import Error
import datetime
import random

def connect_database(database):
    """
    This function creates the database, or connects to the
    existing database

    database: Name of the database
    """
    conn = sqlite3.connect(database)
    c = conn.cursor()

    return c

def create_table(c, tablename):
    """
    This function creates the table in the database

    c: cursor
    tablename: table that has to be created
    """
    c.execute("""
    create table if not exists {}
    (unix REAL,
    datestamp TEXT,
    keyword TEXT,
    value REAL)
    """.format(tablename)
    )

def data_entry(c, tablename, dict):
    """
    This function inserts the values into the table

    c: cursor
    tablename: table to which values has to be entered
    dict: dictionary with all the values
    """
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("""
    Insert Into  Values
    (145477565,
    '2019-01-01',
    'pythn',
    5)
    """)
