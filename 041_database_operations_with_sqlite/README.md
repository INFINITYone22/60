# Project Title: Database Operations with SQLite

## Description
This project creates and queries a SQLite database.

## Learning Objectives
- Understand how to use the `sqlite3` module in Python.
- Learn how to connect to a database, create tables, insert data, and query data.
- Implement basic database operations using SQLite.

## Prerequisites
- Python installed on your system.
- Basic knowledge of SQL and the `sqlite3` module.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.
4.  Run the program using the command `python main.py`.

## Code Explanation
- The program imports the `sqlite3` module.
- It connects to the database using `sqlite3.connect()`.
- It creates a cursor object using `conn.cursor()`.
- It executes SQL commands to create a table, insert data, and query data.
- It fetches the results of the query using `cursor.fetchall()`.
- It prints the results to the console.
- It closes the connection using `conn.close()`.

## Extensions
- Add more complex SQL queries.
- Implement a GUI using Tkinter.
- Allow the user to specify the database name, table name, and data to be inserted.

## References
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
