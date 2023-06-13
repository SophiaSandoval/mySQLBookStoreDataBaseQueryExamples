import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='project2',
                                         user='root',
                                         password='Oranges1331')

    if connection.is_connected():
        query2 = """ CREATE TABLE customers
        (custID INT (5) NOT NULL,
        custName VARCHAR (30) NOT NULL, 
        zip INT (5) NULL, 
        city VARCHAR (30) NULL, 
        state VARCHAR (30) NULL, 
        PRIMARY KEY(custID));
                    """ 
        cursor = connection.cursor()
        cursor.execute(query2)
        connection.commit()
        print('Customers created successfully')

except Error as e:
   print("Error connecting")
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Connection closed")