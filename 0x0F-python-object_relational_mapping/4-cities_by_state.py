#!/usr/bin/python3

""" a  script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys
if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1], password=sys.argv[2], database=sys.argv[3], port=3306)

    curso = database.cursor()
    curso.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id=cities.state_id")
    cities = curso.fetchall()
    for city in cities:
        print(city)

    curso.close()
    database.close()
