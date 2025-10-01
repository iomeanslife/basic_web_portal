import setup_database
import backend_functions
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
database = config.get("Connection","Database")
setup_database.setup_database(database)
backendFunctions = backend_functions.BackendFunctions(database)
