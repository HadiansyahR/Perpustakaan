from Connector import ConnectionManager
from Model.User import User

class ControllerUser:
    conMan = ConnectionManager("perpustakaan")
    # db = conMan.logOn()
    # userCursor = db.cursor()
    query = ''


    def adminLogin(self, username, password):
        if username == 'admin' and password == 'admin123':
            return True

        return False

    def userLogin(self, username, password):
        db = self.conMan.logOn()
        userCursor = db.cursor()

        query = "SELECT * FROM user"
        listUser = []

        userCursor.execute(query)
        res = userCursor.fetchall()

        for row in res:
            user = User(row[0], row[1], row[2])
            listUser.append(user)

        for user in listUser:
            if (username == user.username and password == user.password) and (username != 'admin' and password != 'admin123'):
                db.close()
                return True
        db.close()
        return False
