import sqlite3

class DatabaseConnection():
    def __init__(self, db_path: str = "aquarium.db"):
        self._connection = sqlite3.connect(db_path, check_same_thread=False)
        self._connection.row_factory = sqlite3.Row

    @property
    def connection(self):
        return self._connection

    def close(self):
        self._connection.close()
