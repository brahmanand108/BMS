import mysql.connector as mycon


#Connect to DB
mydb = mycon.connect(host="localhost", user="root", password="brah@1805", database="BMS_DB" )

print(mydb, "connection established")

