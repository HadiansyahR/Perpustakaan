from Connector import ConnectionManager
from Model.User import User

class ControllerUser:
    conMan = ConnectionManager("perpustakaan")
    db = conMan.logOn()

    userCursor = db.cursor()
    query = ''


    def adminLogin(self, username, password):
        if username == 'admin' and password == 'admin123':
            return True

        return False

    def userLogin(self, username, password):
        query = "SELECT * FROM user"
        listUser = []

        self.userCursor.execute(query)
        res = self.userCursor.fetchall()

        for row in res:
            user = User(row[0], row[1], row[2])
            listUser.append(user)

        for user in listUser:
            if (username == user.username and password == user.password) and (username != 'admin' and password != 'admin123'):
                return True

        return False




        # print(self.userCursor.rowcount)
        #
        # for row in res:
        #     print("Id = ", row[0])
        #     print("Username = ", row[1])
        #     print("Password = ", row[2])

        # rowNum = self.userCursor.execute(query)
        # print(rowNum)
        # for i in range(0, rowNum):
        #     result = self.userCursor.fetchone()
        #     print(result)
