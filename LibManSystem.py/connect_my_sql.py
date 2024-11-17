import mysql.connector
from mysql.connector import Error

def connect_database():#Used to connect to my SQL Database
    db_name = 'library_management_system'
    user = 'root'
    password = 'Cjp007Cjp!'
    host = 'localhost'

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
        print("Connected to MySql Database Successfully!")
        return conn

    except Error as e:
        print(f"Error: {e}")
        return None