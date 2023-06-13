import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='project2',
                                         user='root',
                                         password='Oranges1331')
    
   ##Write a query to retrieve the names of all authors who have written books on
##the subject " VISUAL BASIC.NET " but have not written any books on the subject "
##ORACLE DATABASE".
    if connection.is_connected():
        query8 = """SELECT aName
                    FROM authors, subjects, titles, titleAuthors
                    WHERE authors.auID = titleAuthors.auID
                    AND titleAuthors.titleID = titles.titleID
                    AND titles.subID = subjects.subID
                    AND subjects.sname = 'VISUAL BASIC.NET'
                    AND subjects.sname != 'ORACLE DATABASE';
                    """ 
        cursor = connection.cursor()
        cursor.execute(query8)
        for row in cursor.fetchall():
            print(row)

except Error as e:
   print("Error connecting")
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Connection closed")
