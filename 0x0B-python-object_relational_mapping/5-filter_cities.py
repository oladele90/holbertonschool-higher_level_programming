#!/usr/bin/python3
"""5-filter_cities.py"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities INNER JOIN\
        states ON states.id = cities.state_id\
        WHERE states.name = %s ORDER BY cities.id", (argv[4],))
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    cur.close()
    db.close()
