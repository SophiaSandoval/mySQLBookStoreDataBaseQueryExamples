import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='project2',
                                         user='root',
                                         password='Oranges1331')
    
    ###Find the names of all authors who have written a book in a subject that has the
    ###word "Java" in its name.
    if connection.is_connected():
        query6 = """SELECT aName, title, price
                    FROM authors, titles, titleAuthors, subjects
                    WHERE authors.auID = titleAuthors.auID
                    AND titleAuthors.titleID = titles.titleID
                    AND titles.subID = subjects.subID
                    AND subjects.sName LIKE '%Java%';"""
        cursor = connection.cursor()
        cursor.execute(query6)
        for row in cursor.fetchall():
            print(row)

except Error as e:
   print("Error connecting")
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Connection closed")