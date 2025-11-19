import sqlite3
import os

# Path to your database
db_path = os.path.join(os.getcwd(), "transactions.db")

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print("-", table[0])

# For each table, display all rows
for table in tables:
    print(f"\nContents of table '{table[0]}':")
    cursor.execute(f"SELECT * FROM {table[0]}")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No data in this table.")

# Close connection
conn.close()
