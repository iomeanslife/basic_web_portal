import sqlite3

class BackendFunctions:

    def __init__(self, database):
        self.database = database

    def create_user(self, username, hash):
        try:
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            
            check_exists = cursor.execute(f"SELECT username FROM user WHERE username = '{username}' ") 
            if check_exists.fetchone() is not None:
                raise ValueError("Username already exists.")

            cursor.execute(f"INSERT INTO user VALUES('{username}', '{hash}') ")
            connection.commit()

            check_exists = cursor.execute(f"SELECT username FROM user WHERE username = '{username}' ") 
            if check_exists.fetchone() is None:
                raise SystemError("Creating user failed.")

            return True
        except:
            return False
        finally:
            connection.close()

    def login_user(self, username, hash):
        try:
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            
            check_exists = cursor.execute(f"SELECT username,password_hash FROM user WHERE username = '{username}' AND password_hash = '{hash}'") 
            if check_exists.fetchone() is None:
                raise ValueError("wrong password.")
            return True
        except:
            return False
        finally:
            connection.close()