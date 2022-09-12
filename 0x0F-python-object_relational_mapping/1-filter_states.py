#!/usr/bin/python3

"""script that lists all states with a name starting with N (upper N)
"""

import MySQLdb
import sys
if __name__ == "__main__":
    db_user = sys.argv[1]
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=db_user,
                         passwd=db_passwd, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] is 'N':
            print(row)
    cur.close()
    db.close()
