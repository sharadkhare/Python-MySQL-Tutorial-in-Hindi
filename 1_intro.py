""" python needs a MYSql Driver to access the mysql database. """
import mysql.connector

sharaddb= mysql.connector.connect(host="localhost", user="root", password="root")

print(sharaddb)