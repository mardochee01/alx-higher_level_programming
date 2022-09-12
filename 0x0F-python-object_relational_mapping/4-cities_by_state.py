#!/usr/bin/python3
"""
Write a script that lists all states from the database
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
    cur.execute("""
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states
    ON states.id = cities.state_id
    ORDER BY cities.id ASC;
    """)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close
    db.close
