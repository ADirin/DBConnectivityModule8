import mysql.connector
connection = None
# Database connection parameters
db_config = {
    "host": "127.0.0.1",  # Change this to your MariaDB server host
    "port": 3308,
    "user": "root",
    "password": "Test1234",
    "database": "module8demodb",
}

try:
    # Connect to the database
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print("Connected to the database")

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Example: Insert data into the authors table
        insert_author_query = "INSERT INTO authors (author_name) VALUES (%s)"
        author_data = ("John Doe",)
        cursor.execute(insert_author_query, author_data)
        connection.commit()
        print("Data inserted into the authors table")

        # Example: Select data from the authors table
        select_authors_query = "SELECT * FROM authors"
        cursor.execute(select_authors_query)
        authors = cursor.fetchall()
        print("Authors:")
        for author in authors:
            print(author)

        # Close the cursor and the database connection
        cursor.close()
        connection.close()
        print("Database connection closed")

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()
        print("Database connection closed (in the finally block)")
