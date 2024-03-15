#!/usr/bin/python3
""" lists all states with a name starting with N """
import MySQLdb
from sys import argv
if "__name__" == "__main__":
    # make a connetion with mysql
    db = MySQLdb.connect(host=localhost, port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    # # It gives us the ability to have multiple seperate working environments
    # through the same connection to the database.
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        row[1].startswith("N")
        print(row)
        # clean up process
        cur.close()
        conn.close()
