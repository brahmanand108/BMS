import mysql.connector

'''
pip list : to check the list of imported modules 

To install the mysql connector use the following command 

python.exe -m pipi install --upgrade pip
pip install mysql-connector-python

Installing collected packages: mysql-connector-python
Successfully installed mysql-connector-python-8.3.0

'''


print("Driver is installaed")


'''

Mysql is a package in which connector is a class in which connect is a method.
Using this connect method we are creating the object mydb, in which we are passing 4 parameters 
(host ="" ,
User = "" ,
Password = "" ,
Databse = "")


'''

# Step 1 Create a DB object