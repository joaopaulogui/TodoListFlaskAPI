import mysql.connector

def createDB():
    conn = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'Ronin',
        password = '19122004'
    )

    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS todolist")
    conn.close()