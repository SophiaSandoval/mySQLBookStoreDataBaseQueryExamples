import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='project2',
                                         user='root',
                                         password='Oranges1331')
    if connection.is_connected():
        query4 = """SELECT authors.aName, COUNT(*) AS bookCount
                    FROM authors
                    JOIN titleauthors ON authors.auID = titleauthors.auID
                    GROUP BY authors.aName
                    ORDER BY bookCount DESC
                    LIMIT 1;"""
        cursor = connection.cursor()
        cursor.execute(query4)
        for row in cursor.fetchall():
            print(row)

except Error as e:
   print("Error connecting")
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Connection closed")
