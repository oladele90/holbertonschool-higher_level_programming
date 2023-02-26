#!/usr/bin/python3
"""0-select-states.py"""
import MySQLdb
if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user="root", port=3306,
                         passwd="root", db="hbtn_0e_0_usa")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
