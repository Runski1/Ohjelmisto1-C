import mysql.connector
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='kadonnut_testamentti',
    user='root',
    password='MariaDB',
    autocommit=True
)