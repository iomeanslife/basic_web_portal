import sqlite3

class BackendFunctions:

    def __init__(self, database):
        self.database = database

    def create_user(self, username, hash):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute(f"INSERT INTO user VALUES('{username}', '{hash}') ") # TODO: check if user exists already.
        
        result = cursor.execute("SELECT name FROM sqlite_master WHERE name='user'")
