#!/usr/bin/python3
"""module to test MySQLdb in python script"""
from sys import argv
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute('DESCRIBE states')
    print(cur.fetchall())
    cur.close()
    db.close()
