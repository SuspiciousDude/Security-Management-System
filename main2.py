import sqlite3
import datetime

# Create or connect to the SQLite database
conn = sqlite3.connect("school_security.db")
cursor = conn.cursor()

# Create the 'visitors' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS visitors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        purpose TEXT,
        timestamp DATETIME
    )
''')
conn.commit()

# Function to add a visitor to the database
def add_visitor():
    print("Add Visitor:")
    name = input("Visitor's Name: ")
    purpose = input("Purpose of Visit: ")
    timestamp = datetime.datetime.now()
    
    cursor.execute("INSERT INTO visitors (name, purpose, timestamp) VALUES (?, ?, ?)",
                   (name, purpose, timestamp))
    conn.commit()
    
    print("Visitor added successfully!\n")

# Function to view visitor logs
def view_visitors():
    cursor.execute("SELECT * FROM visitors")
    records = cursor.fetchall()
    
    if not records:
        print("No visitor records found.\n")
        return

    print("Visitor Logs:")
    for record in records:
        entry_id, name, purpose, timestamp = record
        print(f"Entry {entry_id}:")
        print(f"Name: {name}")
        print(f"Purpose: {purpose}")
        print(f"Timestamp: {timestamp}")
        print()

# Main program loop
while True:
    print("School Security Management System")
    print("1. Add Visitor")
    print("2. View Visitor Logs")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_visitor()
    elif choice == '2':
        view_visitors()
    elif choice == '3':
        print("Exiting the program.")
        conn.close()  # Close the database connection before exiting
        break
    else:
        print("Invalid choice. Please try again.\n")
