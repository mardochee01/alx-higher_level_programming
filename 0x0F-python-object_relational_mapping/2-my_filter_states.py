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
    state_name_searched=sys.argv[4]
    db = MySQLdb.connect(user=db_user, passwd=db_password,
                         db=db_name)
    cur = db.cursor()
    cur.execute("""SELECT * FROM `states` 
                WHERE `name` = '{}' 
                ORDER BY `id`""".format(state_name_searched))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == state_name_searched:
            print(row)
    cur.close()
    db.close()
