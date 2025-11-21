import mysql.connector
from mysql.connector import Error

def connect_db():
    """
    Establish a connection to the MySQL database.
    Returns a mysql.connector.connect object if successful, otherwise None.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin123",  # 🔑 Replace with your actual root password
            database="fletapp"
        )
        if connection.is_connected():
            print("✅ Successfully connected to the fletapp database.")
            return connection
    except Error as e:
        print(f"❌ Error while connecting to MySQL: {e}")
        return None
