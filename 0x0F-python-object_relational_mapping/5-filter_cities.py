#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=db_user, passwd=db_password, db=db_name)
    cur = db.cursor()
    cur.execute("""
    SELECT cities.name
    FROM cities
    JOIN states
    ON states.id = cities.state_id
    WHERE states.name = %(state_name)s
    ORDER BY cities.id ASC;
    """, {'mysql_state': state_name})
    query_rows = cur.fetchall()
    listx = []
    for row in query_rows:
        listx.append(row[0])
    print(", ".join(listx))
    cur.close()
    db.close()
