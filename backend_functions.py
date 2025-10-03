import sqlite3

class BackendFunctions:

    def __init__(self, database):
        self.database = database

    def create_user(self, username, hash):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        
        check_exists = cursor.execute(f"SELECT username FROM user WHERE username = '{username}' ") 
        if check_exists.fetchone() is not None:
            raise ValueError("username already exists.")

        cursor.execute(f"INSERT INTO user VALUES('{username}', '{hash}') ") # TODO: check if user exists already.
        connection.commit()
        connection.close()