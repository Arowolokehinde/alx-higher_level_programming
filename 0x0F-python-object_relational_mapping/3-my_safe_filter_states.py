#!/usr/bin/python3

"""  script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections! """

import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1], password=sys.argv[2], database=sys.argv[3], port=3306)

    curso = database.cursor()
    match = sys.argv[4]
    curso.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))

    states = curso.fetchall()
    for state in states:
        print(state)
    curso.close()
    database.close()
