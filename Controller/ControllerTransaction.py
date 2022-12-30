# Import class yang dibutuhkan
from Connector import ConnectionManager
from Model.Transaction import Transaction
from Model.Book import Book
from Model.User import User


# Definisi class ControllerTransaction
class ControllerTransaction:
    # Buat Object Connection Manager dengan argumen perpustakaan, perpustakaan ini nama databasenya
    conMan = ConnectionManager("perpustakaan")

    # Buat variable query yang nantinya akan digunakan sebagai tempat menyimpan query
    query = ''

    # Buat method pinjamBuku untuk melakukan aksi pinjam buku
    # Parameternya ada self, name dan listbook
    # Self memungkinkan kita untuk mengakses ke atribut dan method pada setiap objek yang dibuat
    # Name untuk menampilkan nama user yang login
    # Listbook berisi data buku yang diambil dari method readBook
    def pinjamBuku(self, name, listbook):
        db = self.conMan.logOn()
        transCursor = db.cursor()
        dataStatus = False

        print('\nPEMINJAMAN BUKU\n')
        book_id = input('Masukkan ID Buku yang akan dipinjam: ')

        query = "SELECT * FROM user WHERE username = '%s'" % name
        transCursor.execute(query)
        res = transCursor.fetchall()

        for row in res:
            objUser = User(row[0], row[1], row[2])

        for book in listbook:
            if book_id == book.book_id:
                dataStatus = True
                objBook = Book(book.book_id, book.book_name, book.book_genre, book.quantity)
                objTran = Transaction('', objUser.id, objBook.book_id)
                break
            else:
                dataStatus = False

        if not dataStatus:
            print('Data Tidak Ada')
            db.close()
        else:
            if objBook.quantity == 0:
                print('Maaf buku habis')
                db.close()
            else:
                query = "INSERT INTO transaction VALUES (NULL, '%s', '%s', '%s', '%s')" \
                        % (objUser.id, objBook.book_id, objTran.borrow_date, objTran.return_date)
                transCursor.execute(query)
                db.commit()

                query = "UPDATE book SET quantity = quantity-1 WHERE book_id = '%s'" % objBook.book_id
                transCursor.execute(query)
                db.commit()

                if transCursor.rowcount > 0:
                    print('Peminjaman Berhasil!!!')
                db.close()

    # Buat method readTransaction untuk melihat data transaksi user
    def readTransaction(self, name):
        db = self.conMan.logOn()
        transCursor = db.cursor()
        print("\nDATA PEMINJAMAN USER:", name, "\n")

        listTrans = []

        query = "SELECT * FROM user WHERE username = '%s'" % name
        transCursor.execute(query)
        res = transCursor.fetchall()

        for row in res:
            objUser = User(row[0], row[1], row[2])

        # query = "SELECT COUNT(*) from transaction WHERE user_id = '%s'" % objUser.id
        # self.transCursor.execute(query)
        # res = self.transCursor.fetchall()

        query = "SELECT transaction.transaction_id, user.username, book.book_name, transaction.borrow_date, " \
                "transaction.return_date FROM ((user INNER JOIN transaction ON user.user_id = transaction.user_id) " \
                "INNER JOIN book ON transaction.book_id = book.book_id) WHERE user.user_id = '%s'" % objUser.id

        transCursor.execute(query)
        res = transCursor.fetchall()

        if len(res) < 1:
            print("User belum pernah melakukan peminjaman buku...")
            db.close()
        else:
            for row in res:
                objTrans = Transaction(row[0], row[1], row[2])
                listTrans.append(objTrans)

            print(
                '%s\t%s\t%s\t\t\t\t%s\t%s' % ('Transaction ID', 'Username', 'Book Name', 'Borrow Date', 'Return Date'))

            for trans in listTrans:
                trans_id = trans.transaction_id
                username = trans.user_id
                book_name = trans.book_id
                borrow_date = trans.borrow_date
                return_date = trans.return_date

                if len(book_name) < 8:
                    print(f"{trans_id}\t\t\t\t{username}\t\t{book_name}\t\t\t\t\t{borrow_date}\t{return_date}")
                elif len(book_name) >= 8 and len(book_name) < 12:
                    print(f"{trans_id}\t\t\t\t{username}\t\t{book_name}\t\t\t\t{borrow_date}\t{return_date}")
                elif len(book_name) >= 12 and len(book_name) < 16:
                    print(f"{trans_id}\t\t\t\t{username}\t\t{book_name}\t\t\t{borrow_date}\t{return_date}")
                elif len(book_name) >= 16 and len(book_name) < 20:
                    print(f"{trans_id}\t\t\t\t{username}\t\t{book_name}\t\t{borrow_date}\t{return_date}")
                else:
                    print(f"{trans_id}\t\t\t\t{username}\t\t{book_name}\t{borrow_date}\t{return_date}")

            db.close()
