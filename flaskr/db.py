import sqlite3
DATABASE = "database.db"

def create_timaLogs_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS timeLogs (ID, date, time)")
    con.close()