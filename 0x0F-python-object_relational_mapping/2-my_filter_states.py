#!/usr/bin/python

"""script that takes in an argument
and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=db_user, passwd=db_password, db=db_name)
    cursor = db.cursor()
    sqlquery = ("""SELECT * FROM states WHERE
                BINARY states.name='{}'""".format(state_name))
    cursor.execute(sqlquery)
    data = cursor.fetchall()
    for states in data:
        print(states)
    cursor.close()
    db.close()
