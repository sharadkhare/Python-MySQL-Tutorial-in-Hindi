import mysql.connector

sharaddb= mysql.connector.connect(host="localhost", user="root", password="root")

""" Here now we will create a database """
sharadcursor=sharaddb.cursor()
# sharadcursor.execute("create database sharaddatabase")

""" checking if the database exists or not """

sharadcursor.execute("show databases")

for i in sharadcursor:
    print(i)
