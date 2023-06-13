import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='project2',
                                         user='root',
                                         password='Oranges1331')
    
   ## Find the names of all authors who have written a book with a price between
    ##than $475 and $500 and a cover type of "Paper back"
    if connection.is_connected():
        query7 = """SELECT aName
                    FROM authors, titles, titleAuthors
                    WHERE authors.auID = titleAuthors.auID
                    AND titleAuthors.titleID = titles.titleID
                    AND titles.cover = 'PAPER BACK'
                    and titles.price BETWEEN 475 and 500;
                    """
        cursor = connection.cursor()
        cursor.execute(query7)
        for row in cursor.fetchall():
            print(row)

except Error as e:
   print("Error connecting")
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Connection closed")