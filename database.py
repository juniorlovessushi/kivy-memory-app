import sqlite3

DB_NAME = "storage.db"

def init_db():
    """Create the database table if it does not exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_timestamp(timestamp_str):
    """Insert a new timestamp record."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (timestamp) VALUES (?)", (timestamp_str,))
    conn.commit()
    conn.close()

def get_last_timestamp():
    """Retrieve the most recent timestamp."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp FROM logs ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else "No history recorded yet."
