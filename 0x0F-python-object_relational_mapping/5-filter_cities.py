#!/usr/bin/python3
"""module to test MySQLdb in python scripts"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities WHERE cities.state_id IN\
                (SELECT states.id FROM states WHERE states.name = %s)",
                (argv[4],))
    rows = cur.fetchall()
    length = len(rows)
    for i in range(length):
        if i == (length - 1):
            print(rows[i][0], end="")
        else:
            print(rows[i][0], end=", ")
    print()
