from Controller.ControllerUser import ControllerUser
from View.AdminView import AdminView
from View.UserView import UserView


class LoginView:

    @staticmethod
    def menuLogin():
        user1 = ControllerUser()
        loginStatus = False

        while True:
            print('LOGIN PAGE')
            print('\nMenu:')
            print('1. Login Sebagai Admin\n2. Login Sebagai User\n')
            pil = input('Masukkan pilihan: ')

            match pil:
                case '1':
                    username = input('\nMasukkan Username: ')
                    password = input('Masukkan Password: ')
                    if user1.adminLogin(username, password):
                        print('\nBerhasil masuk sebagai', username)
                        admView = AdminView()
                        admView.menu(username)
                        break
                    else:
                        print('Login gagal, silahkan coba lagi\n')
                case '2':
                    username = input('\nMasukkan Username: ')
                    password = input('Masukkan Password: ')
                    if user1.userLogin(username, password):
                        print('\nBerhasil masuk sebagai', username)
                        userView = UserView()
                        userView.menuUser(username)
                        break
                    else:
                        print('Login gagal, silahkan coba lagi\n')
                case _:
                    print('Input Salah\n')
