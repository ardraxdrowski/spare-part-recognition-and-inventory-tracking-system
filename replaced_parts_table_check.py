import sqlite3

conn = sqlite3.connect("database/part_details.db")
cursor = conn.cursor()

cursor.execute("""
    select * from 
    parts_details         
    """)
print(cursor.fetchall())


conn.close()