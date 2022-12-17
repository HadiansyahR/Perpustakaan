from Controller.ControllerBook import ControllerBook
from Controller.ControllerTransaction import ControllerTransaction


class UserView:

    def menuUser(self, name):
        conBook = ControllerBook()
        conTran = ControllerTransaction()

        print('\nWelcome', name)
        while True:
            print('\nMenu:')
            print('1. Lihat Data Buku\n2. Pinjam Buku\n3. Lihat Data Peminjaman\n0. Keluar')
            pil = input('Masukkan pilihan: ')
            match pil:
                case '1':
                    conBook.readBook()
                    if not UserView.continueUser():
                        print('Terimakasih telah menggunakan program kami')
                        break
                case '2':
                    listBook = conBook.readBook()
                    conTran.pinjamBuku(name, listBook)
                    conBook.readBook()
                    if not UserView.continueUser():
                        print('Terimakasih telah menggunakan program kami')
                        break
                case '3':
                    conTran.readTransaction(name)
                    if not UserView.continueUser():
                        print('Terimakasih telah menggunakan program kami')
                        break
                case '0':
                    print('Terimakasih telah menggunakan program kami')
                    break
                case _:
                    print('\nInput Salah')

    @staticmethod
    def continueUser():
        continuePil = input('Apakah anda ingin melanjutkan? (Y/N): ')

        if continuePil == 'Y' or continuePil == 'y':
            return True
        else:
            return False