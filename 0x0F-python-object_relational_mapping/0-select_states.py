#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

if "__name__" == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    # It gives us the ability to have multiple seperate working environments
    # through the same connection to the database.
    cur = db.cursor()
    cur.execute("SELECT * FROM STATES")
    query_rows = cur.fetchall()
    for i in rows:
        print(i)
        # close the process
        cur.close()
        conn.close()
