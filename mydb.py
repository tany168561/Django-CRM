import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'

)

# prer a c
cursorOject = dataBase.cursor()

cursorOject.execute("CREATE DATABASE elderco")

print("All Done!")
