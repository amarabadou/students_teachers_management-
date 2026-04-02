import mysql.connector
from mysql.connector import Error
# for database connection
def create_connection(database=None):
    
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",# replaced with your DB username
            password="password", # replaced with your DB password
            db = "DB_NAME" # replaced with your DB name
        )
        cursor = connection.cursor()
        if database:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
            connection.database = database
        print("connection success")
        return connection
    except Error as e:
        print("error", e)
        return None
