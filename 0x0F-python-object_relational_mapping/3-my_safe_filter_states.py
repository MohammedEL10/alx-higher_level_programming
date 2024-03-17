#!/usr/bin/python3
""" it’s an SQL injection to delete all records of a table…"""
import MySQLdb
from sys import argv

#the code shold not be executed when imported
if "__name__" == "__main__":

    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwod=argv[2], db=argv[3])

    # It gives us the ability to have multiple seperate working environment
    # through the same connection to the database.
    cur = db.cursur()
    nmeSr = "SELECT * FROM states WHERE name= %s" [argv[4]]

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean up process
        cur.close()
        db.close()
