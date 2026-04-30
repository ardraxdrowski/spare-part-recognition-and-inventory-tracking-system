import sqlite3

conn = sqlite3.connect("database/part_details.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS replaced_parts (
    sno INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    part_name TEXT,
    quantity INTEGER,
    reason TEXT,
    warranty_status TEXT,
    criticality_level TEXT
)
""")

conn.commit()
conn.close()

print("replaced_parts table ready")