import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT UNIQUE
)
""")

conn.commit()


def insert_data(content):
    try:
        cursor.execute("INSERT INTO data (content) VALUES (?)", (content,))
        conn.commit()
        return True
    except:
        return False


def get_all_data():
    cursor.execute("SELECT * FROM data")
    return cursor.fetchall()