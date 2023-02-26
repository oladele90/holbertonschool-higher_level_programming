#!/usr/bin/python3
"""4-cities_by_state.py"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name,\
        states.name FROM cities INNER JOIN\
        states ON states.id = cities.state_id ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
