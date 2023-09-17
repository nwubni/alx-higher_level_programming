#!/usr/bin/python3
"""
This module gets th id and name of states
from the states table
"""

from sys import argv
import MySQLdb

if (__name__ == "__main__"):
    conn = MySQLdb.connect(user=argv[1],
                           passwd=argv[2],
                           db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states;")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
