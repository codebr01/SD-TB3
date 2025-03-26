import sqlite3
import os

db_path = "./images.db"

conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS images (
    id TEXT PRIMARY KEY,
    date TEXT,
    time TEXT,
    original_path TEXT,
    processed_path TEXT
)''')
conn.commit()
conn.close()