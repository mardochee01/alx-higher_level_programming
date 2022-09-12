#!/usr/bin/python

"""script that takes in an argument 
and displays all values in the states table 
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db_user = sys.argv[1]
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=db_user,
                         passwd=db_passwd, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id".
                format(state_name))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == state_name:
            print(row)
    cur.close()
    db.close()
