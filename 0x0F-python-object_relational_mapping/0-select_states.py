#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    script that lists all states from the database hbtn_0e_0_usa
    """
    database_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    database_cursor = database_connect.cursor()

    database_cursor.execute("SELECT * FROM states")

    rows_selected = database_cursor.fetchall()

    for row in rows_selected:
        print(row)
