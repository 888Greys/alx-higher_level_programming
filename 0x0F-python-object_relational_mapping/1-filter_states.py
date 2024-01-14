#!/usr/bin/python3
"""
script that lists all states with a name
starting with N (upper N) from the
database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

"""
script that lists all states with a name
starting with N (upper N) from the
database hbtn_0e_0_usa
"""

if __name__ == '__main__':
    database_connect = MySQLdb.connect(
            host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    database_cursor = database_connect.cursor()

    database_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    rows_selected = database_cursor.fetchall()

    for row in rows_selected:
        print(row)
