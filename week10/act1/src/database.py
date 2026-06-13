import sqlite3

class Database:
    """Small wrapper around the SQLite database path used by the managers."""

    def __init__(self, db_path=":memory:"):
        self.db_path = db_path

    def get_connection(self):
        # Managers open short-lived connections so each operation commits or rolls back cleanly.
        return sqlite3.connect(self.db_path)

    
