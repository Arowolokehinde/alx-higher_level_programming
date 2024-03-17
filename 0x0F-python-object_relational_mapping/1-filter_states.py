#!/usr/bin/python3

""" a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:"""

import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1], password=sys.argv[2], database=sys.argv[3], port=3306)

    curso = database.cursor()
    curso.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    states = curso.fetchall()
    for state in states:
        print(state)

    curso.close()
    database.close()
