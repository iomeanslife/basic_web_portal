import sqlite3

con = sqlite3.connect("small_database.db")
cur = con.cursor()

res = cur.execute("SELECT name FROM sqlite_master WHERE name='user'")
fetched = res.fetchone()
if res.rowcount > 0:
    cur.execute("CREATE TABLE user(username,password_hash)")