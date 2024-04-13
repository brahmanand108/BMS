
import mysql.connector as mycon

# Create DB

'''
cursor() method is used to intract with the databse

'''

db_cursor = mydb.cursor()
db_cursor.execute ("CREATE DATABSE BMS_DB")


# Create table


db_cursor.execute ("CREATE TABLE customer_mgmt(id INT AUTO_INCREMENT PRIMARY KEY, order_id INT,name VARCHAR(255), order VARCHAR (255),Quantity INT, date )")

print("Table created")


# Show table

db_cursor("SHOW TABLE")
for i in db_cursor:
    print(i)