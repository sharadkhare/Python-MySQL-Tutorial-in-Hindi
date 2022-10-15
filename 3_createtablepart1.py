import mysql.connector

sharaddb= mysql.connector.connect(host="localhost", user="root", password="root", database="sharaddatabase")

sharadcursor=sharaddb.cursor()
sharadcursor.execute("show tables")

for i in sharadcursor:
    print(i)



