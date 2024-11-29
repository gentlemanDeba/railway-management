from config import get_db_connection

class Database:
    def __init__(self):
        self.connection = get_db_connection()
        if self.connection is not None:
            self.cursor = self.connection.cursor()
        else:
            self.cursor = None

    def execute_query(self, query, params=None):
        if self.cursor:
            self.cursor.execute(query, params or ())
            self.connection.commit()

    def fetch_all(self, query, params=None):
        if self.cursor:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        return []

    def is_connected(self):
        return self.connection and self.connection.is_connected()
