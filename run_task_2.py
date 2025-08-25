#!/usr/bin/env python3
"""
Script to execute task_2.sql and create tables in alx_book_store database
"""

import mysql.connector
from mysql.connector import Error


def execute_sql_file():
    """
    Executes the task_2.sql file to create all tables
    """
    connection = None
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Read the SQL file
            with open('task_2.sql', 'r') as file:
                sql_commands = file.read()
            
            # Split commands by semicolon and execute each
            commands = sql_commands.split(';')
            
            for command in commands:
                command = command.strip()
                if command:  # Skip empty commands
                    cursor.execute(command)
                    print(f"Executed: {command[:50]}...")
            
            connection.commit()
            print("All tables created successfully!")
            
            cursor.close()
            
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    execute_sql_file()

