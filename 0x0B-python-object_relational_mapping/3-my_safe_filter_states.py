#!/usr/bin/python3
"""3-my_safe_filter_states.py"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE NAME = %s ORDER BY id", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        for col in row:
            if type(col) is not int:
                if col == argv[4]:
                    print(row)
    cur.close()
    db.close()
