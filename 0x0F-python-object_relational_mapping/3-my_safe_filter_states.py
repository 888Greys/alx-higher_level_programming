#!/usr/bin/python3
"""
script should take 4 arguments:
mysql username, mysql password,
database name and state name searched
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    database_connect = db.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    database_cursor = database_connect.cursor()
    database_cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows_selected = database_cursor.fetchall()

    for row in rows_selected:
        print(row)
