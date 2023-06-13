import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='project2',
                                         user='root',
                                         password='Oranges1331')
    if connection.is_connected():
        query3 = """INSERT INTO Customers (custID, custName, zip, city, state)
                VALUES (1, 'ABRAHAM SILBERSCHATZ', 92373, 'Redlands', 'CA'), 
                 (2, ' HENRY KORTH ', 92401, 'San Bernardino', 'CA')
                 (3, 'CALVIN HARRIS', 92341, 'Los Angeles', 'CA'), 
                 (4, 'MARTIN GARRIX', 95674, 'San Diego', 'CA'), 
                (5,  'JAMES GOODWILL', 94372, 'San Francisco', 'CA');"""
        cursor = connection.cursor()
        cursor.execute(query3)
        cursor.commit()
        print('DATA INSERTED')

except Error as e:
   print("Error connecting")
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Connection closed")

