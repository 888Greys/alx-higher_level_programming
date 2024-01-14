#!/usr/bin/python3

"""
    Lists all states from the database hbtn_0e_0_usa.
    Usage: ./0-select_states.py <mysql username> \
                             <mysql password> \
                             <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":

    """
    Accesses the database and gets the states from the database
    """

    database_connect = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    database_cursor = database_connect.cursor()
    database_cursor.execute("SELECT * FROM `states`")
    [print(state) for state in database_cursor.fetchall()]
