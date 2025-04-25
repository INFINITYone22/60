# Project Title: ORM with SQLAlchemy

## Description
This project uses SQLAlchemy for database operations.

## Learning Objectives
- Understand how to use SQLAlchemy as an ORM.
- Learn how to define models, create tables, insert data, and query data using SQLAlchemy.

## Prerequisites
- Python installed on your system.
- Basic knowledge of SQL and ORMs.

## Setup Instructions
1.  Make sure Python is installed and accessible in your system's PATH.
2.  Open a terminal or command prompt.
3.  Navigate to the project directory.
4.  Install the `SQLAlchemy` library using the command `pip install SQLAlchemy`.
5.  Run the program using the command `python main.py`.

## Code Explanation
- The program imports the necessary modules from `sqlalchemy`.
- It defines the database engine using `create_engine()`.
- It defines the base class for declarative models using `declarative_base()`.
- It defines the `User` model with columns for `id`, `name`, and `age`.
- It creates the table in the database using `Base.metadata.create_all()`.
- It creates a session using `sessionmaker()`.
- It creates new users and adds them to the session.
- It commits the changes to the database using `session.commit()`.
- It queries the users using `session.query()` and prints the results.
- It closes the session using `session.close()`.

## Extensions
- Add more complex models and relationships.
- Implement a GUI using Tkinter.
- Allow the user to perform different database operations.

## References
- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)
- [Real Python](https://realpython.com/)
