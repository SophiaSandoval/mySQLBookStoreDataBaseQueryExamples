import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='project2',
                                         user='root',
                                         password='Oranges1331')
###Form a query to decrease the price of all the books published before 2003 by
###25% and decrease the price of all the books published after 2004 by 10%
  ### AFTER RUN SELECT * FROM titles
    if connection.is_connected():
        query10 = """UPDATE titles
                SET price = CASE 
                WHEN 'pubDate' < '2003-01-01' THEN price * 0.75
                 WHEN 'pubDate' > '2004-12-31' THEN price * 0.9
                 ELSE price
                END;
                    """ 
        cursor = connection.cursor()
        cursor.execute(query10)
        connection.commit()
        for row in cursor.fetchall():
            print(row)

except Error as e:
   print("Error connecting")
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Connection closed")