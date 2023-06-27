#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username, password, database = sys.argv[1:]

    # Connect to the MySQL server and execute the query
    with MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    ) as db:
        with db.cursor() as cursor:
            # Execute the SQL query
            query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
            cursor.execute(query)

            # Fetch all the rows returned by the query
            results = cursor.fetchall()

            # Print the results
            for row in results:
                print(row)
