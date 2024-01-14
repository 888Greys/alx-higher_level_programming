#!/usr/bin/python3
"""
a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    It Access to the database and get the states
    from the database.
    """
    database_connect = db.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    database_cursor = database_connect.cursor()

    database_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
                        states.id ASC".format(argv[4]))
    row_selected = database_cursor.fetchall()

    for row in row_selected:
        print(row)
