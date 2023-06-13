import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='project2',
                                         user='root',
                                         password='Oranges1331')
    if connection.is_connected():
        query5 = """SELECT pname, title, price
                    FROM publishers, titles
                    WHERE publishers.pubID = titles.pubID;"""
        cursor = connection.cursor()
        cursor.execute(query5)
        for row in cursor.fetchall():
            print(row)

except Error as e:
   print("Error connecting")
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Connection closed")