import mysql.connector

class ConnectionManager:
    user = "root"
    password = ""
    host = "localhost"
    database = ""

    # Constructor atau kerangka dari class ConnectionManager
    def __init__(self, database):
        self.database = database

    def logOn(self):
        # method connect ini mereturn MySQLConnection object jika koneksi berhasil dibuat
        db = mysql.connector.connect(user=self.user, passwd=self.password, host=self.host, database=self.database)
        return db