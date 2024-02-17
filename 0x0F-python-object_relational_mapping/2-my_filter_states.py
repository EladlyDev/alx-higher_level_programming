#!/usr/bin/python3
""" MySQLdb Practicing """
# import mysql.connector as MySQLdb  # cuz I had problem installing mysqldb
import MySQLdb
from sys import argv

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 3306

    if len(argv) >= 5:
        USER = argv[1]
        PASS = argv[2]
        DB = argv[3]

        conn = MySQLdb.connect(host=HOST, port=PORT, user=USER,
                               passwd=PASS, db=DB)
        cur = conn.cursor()
        query = "SELECT id, name FROM states \
        WHERE name LIKE BINARY '{}' \
        ORDER BY id;".format(argv[4])
        cur.execute(query)
        states = cur.fetchall()
        [print(state) for state in states]
    else:
        print("USAGE: {user} {pass} {db} {state name}")
