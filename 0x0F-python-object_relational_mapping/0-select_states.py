#!/usr/bin/python3

""" list the states by  id  from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            port=3306
            )

    curso = database.cursor()
    curso.execute("SELECT * FROM states")
    states = curso.fetchall()
    for state in states:
        print(state)

    curso.close()
    database.close()
