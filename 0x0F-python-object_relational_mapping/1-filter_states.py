#!/usr/bin/python3
"""
Gets states entries starting with the letter N
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        with MySQLdb.connect(user=username, passwd=password, db=database) as conn:
            with conn.cur() as cur:
                q = "SELECT id, name FROM states WHERE BINARY name LIKE %s;"
                cur.execute(q, ("N%",))
                rows = cur.fetchall()

                for row in rows:
                    print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
