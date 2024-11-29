import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        rpwd = input("Enter MySQL root password: ")
        sqlcon = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=rpwd,
            database="Railway_Records"
        )
        if sqlcon.is_connected():
            print(" Successful...")
            print("***************************************\n\n")
            return sqlcon
    except Error as e:
        print(f"Error: {e}")
        print("Failed to connect to the database. Please check your credentials and try again.")
        return None
