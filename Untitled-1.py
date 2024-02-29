import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM Note")
# cursor.execute("DELETE FROM Note")

# Fetch data from the executed query
data = cursor.fetchall()

# Do something with the fetched data
for row in data:
    print(row)

# Close the cursor and the connection
cursor.close()
conn.close()