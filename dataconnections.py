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
import time

def connect_database(database):
    """
    This function creates the database, or connects to the
    existing database

    database: Name of the database
    """
    conn = sqlite3.connect(database)
    c = conn.cursor()

    return c, conn

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
    name TEXT,
    address TEXT,
    mobile TEXT,
    email TEXT,
    github TEXT,
    linkedin TEXT,
    expertise TEXT,
    similarity_score REAL)
    """.format(tablename)
    )

def data_entry(c, conn, tablename, cont):
    """
    This function inserts the values into the table

    c: cursor
    tablename: table to which values has to be entered
    dict: dictionary with all the values
    """
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    name = str(cont['name'])
    address = str(cont['address'])
    mobile = str(cont['mobile'])
    email = str(cont['email'])
    github = str(cont['github'])
    linkedin = str(cont['linkedin'])
    expertise = str(cont['expertise'])
    similarity_score = float(cont['similarity_score'])
    c.execute("""
    Insert Into {}
    (unix,
    datestamp,
    name,
    address,
    mobile,
    email,
    github,
    linkedin,
    expertise,
    similarity_score)
    VALUES
    (
    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
    )
    """.format(tablename), (unix, date, name, address, mobile, email, github, linkedin, expertise, similarity_score))
    conn.commit()
    c.close()
    conn.close()

if __name__ == '__main__':
    print("Importing database functions")
