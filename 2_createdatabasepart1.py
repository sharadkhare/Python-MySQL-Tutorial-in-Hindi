import mysql.connector

sharaddb= mysql.connector.connect(host="localhost", user="root", password="root", database="sharaddatabase")
print(sharaddb)