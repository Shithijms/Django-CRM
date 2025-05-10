# pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
        passwd = 'SMS2305',
        user = 'root',
        host = 'localhost',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")