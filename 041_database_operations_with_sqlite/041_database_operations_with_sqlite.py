import sqlite3

def database_operations_with_sqlite():
    # Connect to the database
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
    ''')

    # Insert data into the table
    cursor.execute("INSERT INTO users (name, age) VALUES ('John Doe', 30)")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Jane Smith', 25)")

    # Commit the changes
    conn.commit()

    # Query the table
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("Users:")
    for row in rows:
        print(row)

    # Close the connection
    conn.close()

database_operations_with_sqlite()
