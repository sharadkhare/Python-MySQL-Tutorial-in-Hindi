import mysql.connector

sharaddb= mysql.connector.connect(host="localhost", user="root", password="root", database="sharaddatabase")

sharadcursor=sharaddb.cursor()
# sharadcursor.execute("create table customers (id int auto_increment primary key, name varchar(255), address varchar(255))")

sharadcursor.execute("alter table customers add column id int auto_increment primary key")

