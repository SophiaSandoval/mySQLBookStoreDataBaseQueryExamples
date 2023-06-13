import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='project2',
                                         user='root',
                                         password='Oranges1331')
##Write a query to retrieve the names of all whose email address contains the
##domain "gmail.com"
  
    if connection.is_connected():
        query9 = """SELECT aName
                    FROM authors
                    WHERE email LIKE '%gmail.com%' ;
                    """ 
        cursor = connection.cursor()
        cursor.execute(query9)
        for row in cursor.fetchall():
            print(row)

except Error as e:
   print("Error connecting")
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Connection closed")