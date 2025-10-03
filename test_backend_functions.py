import unittest
import sqlite3
import configparser
import backend_functions
import setup_database

class TestCreateUser(unittest.TestCase):

    def __init__(self, methodName = "create_user"):
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.database = config.get("Connection","TestDatabase")
        setup_database.setup_database(self.database)
        super().__init__(methodName)
        

    def setUp(self):
        self.clear_user_table()
        return super().setUp()
    
    def test_create_user(self):
        backendFunctions = backend_functions.BackendFunctions(database=self.database)
        backendFunctions.create_user("testUser","testPassword")
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        result = cursor.execute("SELECT username, password_hash FROM user WHERE username = 'testUser' AND password_hash = 'testPassword'") # TODO: fill in with hashvalue for "testPassword".
        self.assertEqual(1,len( result.fetchall()))
        connection.close()
        
    def clear_user_table(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM user")
        connection.commit()
        connection.close()
    
    def tearDown(self):
        self.clear_user_table()
        return super().tearDown()