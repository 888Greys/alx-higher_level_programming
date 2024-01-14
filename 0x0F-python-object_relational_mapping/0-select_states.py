#!/usr/bin/python3

"""
This Script lists all the states from the database
hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    """
    Accesses the database and gets the states from the database
    """

    database_connect = MySQLdb.connect(host="localhost", user=argv[1], port=3306, 
            passwd=argv[2], db=argv[3])

    database_cursor = database_connect.cursor()
    database_cursor.execute("SELECT * FROM states")

    row_selected = database_cursor.fetchall()

    for row in row_selected:
        print(row)
