import mysql.connector

class ConnectionManager:
    user = "root"
    password = ""
    host = "localhost"
    database = ""

    def __init__(self, database):
        self.database = database

    def logOn(self):
        db = mysql.connector.connect(user=self.user, passwd=self.password, host=self.host, database=self.database)
        return db