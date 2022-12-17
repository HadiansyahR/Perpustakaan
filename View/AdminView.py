from Controller.ControllerBook import ControllerBook


class AdminView:

    def menu(self, name):
        conBook = ControllerBook()
        print('\nWelcome', name)
        while True:
            print('\nMenu:')
            print('1. Lihat Data Buku\n2. Masukkan Data Buku\n3. Update Data Buku\n4. Hapus Data Buku\n0. Keluar')
            pil = input('Masukkan pilihan: ')
            match pil:
                case '1':
                    conBook.readBook()
                    if not AdminView.continueAdmin():
                        print('Terimakasih telah menggunakan program kami')
                        break
                case '2':
                    conBook.createBook()
                    if not AdminView.continueAdmin():
                        print('Terimakasih telah menggunakan program kami')
                        break
                case '3':
                    listBook = conBook.readBook()
                    conBook.updateBook(listBook)
                    if not AdminView.continueAdmin():
                        print('Terimakasih telah menggunakan program kami')
                        break
                case '4':
                    listBook = conBook.readBook()
                    conBook.deleteBook(listBook)
                    if not AdminView.continueAdmin():
                        print('Terimakasih telah menggunakan program kami')
                        break
                case '0':
                    print('Terimakasih telah menggunakan program kami')
                    break
                case _:
                    print('\nInput Salah')

    @staticmethod
    def continueAdmin():
        continuePil = input('Apakah anda ingin melanjutkan? (Y/N): ')

        if continuePil == 'Y' or continuePil == 'y':
            return True
        else:
            return False