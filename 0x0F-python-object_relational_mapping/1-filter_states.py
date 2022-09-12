#!/usr/bin/python3

"""script that lists all states with a name starting with N (upper N)
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host ="localhost", port=3306, 
                         user=db_user, passwd=db_password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `states.id` WHERE `states.names` LIKE 'N%'")
    data = cur.fetchall()
    for states in data:
        print(states)
    cur.close()
    db.close()
