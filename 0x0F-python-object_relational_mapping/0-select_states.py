#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa
no argument validation needed
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=db_user, passwd=db_password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `states.id`")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close
    db.close
