import sqlite3
import csv

# Connect to SQLite database
conn = sqlite3.connect('student.db')
cur = conn.cursor()

# Create the student table if it doesn't exist
cur.execute('''
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')

print("Table created successfully!")

# Read from CSV and insert data
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        cur.execute("INSERT INTO student (name, age, grade) VALUES (?, ?, ?)", row)

conn.commit()
print("Data inserted from CSV!")

# Display all records
print("All student records:")
cur.execute("SELECT * FROM student")
for row in cur.fetchall():
    print(row)

# Close the connection
conn.commit()
conn.close()
print("\n All operations completed!")