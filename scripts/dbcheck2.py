import sqlite3

conn = sqlite3.connect("database/part_details.db")
cursor = conn.cursor()
cursor.execute("""
    SELECT * FROM parts_details
               """)
'''cursor.execute("""
    UPDATE parts_details
    SET stock = ?
    WHERE part_name = ?
""", (11, "Control Board CS Smart 90V"))'''
print(cursor.fetchall())
conn.commit()

conn.close()
