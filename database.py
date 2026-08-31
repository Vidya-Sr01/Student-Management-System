import sqlite3

# Connect to the database
connection = sqlite3.connect("students.db")

# Create cursor
cursor = connection.cursor()

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

# Save changes
connection.commit()