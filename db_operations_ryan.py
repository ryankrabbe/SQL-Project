import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = r"C:\Users\Ryan Krabbe\Documents\datafun-05-sql\\project.db"

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # Use the pandas DataFrame to_sql() method to insert data
            # Pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data from CSV:", e)

def insert_records():
    """Function to read and execute SQL statements to insert data"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = r"C:\Users\Ryan Krabbe\Documents\datafun-05-sql\\insert_records.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Data inserted successfully.")
    except sqlite3.Error as e:
        print("Error inserting data from SQL:", e)

def update_records():
    """Function to update one or more records in the authors table"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("update_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Records updated successfully.")
    except sqlite3.Error as e:
        print("Error updating records:", e)

def delete_records():
    """Function to delete records from a table"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("delete_records.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Records deleted successfully.")
    except sqlite3.Error as e:
        print("Error deleting records:", e)

def query_aggregation():
    """Function to perform aggregation functions on the books table"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_aggregation.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            result = cursor.fetchone()
            print("Total Books:", result[0])
            print("Average Year Published:", round(result[1]))
            print("Average Title Length:", round(result[2]), "characters.")
    except sqlite3.Error as e:
        print("Error querying aggregation for books:", e)

def query_filter():
    """Function to filter book data based on conditions"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_filter.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            books = cursor.fetchall()
            for book in books:
                print(book[1], book[2])  # Print title and year_published
    except sqlite3.Error as e:
        print("Error filtering book data:", e)

def query_sorting():
    """Function to sort book data based on publication date"""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_sorting.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            books = cursor.fetchall()
            for book in books:
                print(book[0], book[1])  # Print year_published and title
    except sqlite3.Error as e:
        print("Error sorting book data:", e)

def query_group_by():
    """Function to execute SQL query with GROUP BY clause and display the count of each grouping."""
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_group_by.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.cursor()
            cursor.execute(sql_script)
            results = cursor.fetchall()
            print("Title Length Group\tCount of Books")
            for row in results:
                print(f"{row[0]}\t\t{row[1]}")
            print("Query executed successfully.")
    except sqlite3.Error as e:
        print("Error executing query:", e)

def query_join():
    """Function to read and execute SQL statements to perform INNER JOIN and display the results"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_join.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            rows = cursor.fetchall()
            # Display the joint data
            for row in rows:
                print(f"Title: {row[0]}, Author's Last Name: {row[3]}")
            print("Query executed successfully.")
    except sqlite3.Error as e:
        print("Error executing query:", e)

def main():
    insert_data_from_csv()
    insert_records()
    update_records()
    delete_records()
    query_aggregation()
    query_filter()
    query_sorting()
    query_group_by()
    query_join()

if __name__ == "__main__":
    main()