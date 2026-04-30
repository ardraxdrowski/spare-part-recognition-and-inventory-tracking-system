import sqlite3
import pandas as pd

conn = sqlite3.connect("database/part_details.db")

df = pd.read_sql_query("SELECT * FROM replaced_parts", conn)

df.to_excel("replacement_log.xlsx", index=False)

conn.close()

print("Existing records exported to replacement_log.xlsx")