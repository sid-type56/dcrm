import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd='root@2024'
)

#prepare a cursor object
cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE customermanagement")

print('ALL DONE!!!!')