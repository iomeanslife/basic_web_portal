import sqlite3

def setup_database(database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    result = cursor.execute("SELECT name FROM sqlite_master WHERE name='user'")
    if result.fetchone() is None:
        cursor.execute("CREATE TABLE user(username,password_hash)")
    connection.close()