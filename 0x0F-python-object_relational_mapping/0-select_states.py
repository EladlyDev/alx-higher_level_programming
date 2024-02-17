#!/usr/bin/python3
""" 0-select_states.py """
# import mysql.connector as MySQLdb # cuz I had problem installing mysqldb
import MySQLdb
from sys import argv

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 3306

    if len(argv) >= 4:
        USER = argv[1]
        PASS = argv[2]
        DB = argv[3]

        conn = MySQLdb.connect(host=HOST, port=PORT, user=USER,
                               passwd=PASS, db=DB)
        cur = conn.cursor()
        cur.execute("SELECT * FROM states")
        states = cur.fetchall()
        [print(state) for state in states]
    else:
        print("USAGE: {user} {pass} {db}")
