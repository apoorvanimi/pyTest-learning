# Sample 4: pandas (this loads pandas the first time you run it)
import pandas as pd

df = pd.DataFrame({
    "test_name": ["test_login", "test_checkout", "test_search"],
    "duration_ms": [120, 980, 340],
    "status": ["passed", "failed", "passed"],
})
print(df)
print("\nFailed tests:")
print(df[df["status"] == "failed"])
print("\nAverage duration:", df["duration_ms"].mean())


import sqlite3

connection = sqlite3.connect("test.db")

df = pd.read_sql_query(
    "SELECT * FROM users",
    connection
)

print(df)

connection.close()