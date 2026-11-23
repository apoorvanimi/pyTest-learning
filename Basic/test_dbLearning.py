import sqlite3

connection = sqlite3.connect("test.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        age INTEGER
    )
""")

connection.commit()

users = [
    ("Amit", "amit@test.com", 30),
    ("Neha", "neha@test.com", 28),
    ("Ravi", "ravi@test.com", 35)
]

cursor.executemany("""
    INSERT INTO users (name, email, age)
    VALUES (?, ?, ?)
""", users)


connection.commit()

cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()

for row in rows:
    print(row)

#connection.close()