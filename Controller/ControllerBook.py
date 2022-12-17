from Connector import ConnectionManager
from Model.Book import Book

class ControllerBook:
    conMan = ConnectionManager("perpustakaan")
    # db = conMan.logOn()
    # bookCursor = db.cursor()
    query = ''

    def readBook(self):
        query = "SELECT * FROM book"
        listBook = []

        db = self.conMan.logOn()
        bookCursor = db.cursor()

        bookCursor.execute(query)
        res = bookCursor.fetchall()

        for row in res:
            book = Book(row[0], row[1], row[2], row[3])
            listBook.append(book)
        print('\nDATA BUKU\n')
        print('%s\t%s\t\t\t\t%s\t%s' % ('Book Id', 'Book Name', 'Book Genre', 'Quantity'))

        for book in listBook:
            book_id = book.book_id
            book_name = book.book_name
            book_genre = book.book_genre
            book_quantity = book.quantity
            if len(book_name) < 8:
                if len(book_genre) < 8:
                    print(f"{book_id}\t{book_name}\t\t\t\t\t{book_genre}\t\t{book_quantity}")
                else:
                    print(f"{book_id}\t{book_name}\t\t\t\t\t{book_genre}\t{book_quantity}")
            elif len(book_name) >= 8 and len(book_name) < 12:
                if len(book_genre) < 8:
                    print(f"{book_id}\t{book_name}\t\t\t\t{book_genre}\t\t{book_quantity}")
                else:
                    print(f"{book_id}\t{book_name}\t\t\t\t{book_genre}\t{book_quantity}")
            elif len(book_name) >= 12 and len(book_name) < 16:
                if len(book_genre) < 8:
                    print(f"{book_id}\t{book_name}\t\t\t{book_genre}\t\t{book_quantity}")
                else:
                    print(f"{book_id}\t{book_name}\t\t\t{book_genre}\t{book_quantity}")
            elif len(book_name) >= 16 and len(book_name) < 20:
                if len(book_genre) < 8:
                    print(f"{book_id}\t{book_name}\t\t{book_genre}\t\t{book_quantity}")
                else:
                    print(f"{book_id}\t{book_name}\t\t{book_genre}\t{book_quantity}")
            else:
                if len(book_genre) < 8:
                    print(f"{book_id}\t{book_name}\t{book_genre}\t\t{book_quantity}")
                else:
                    print(f"{book_id}\t{book_name}\t{book_genre}\t{book_quantity}")
        return listBook

    def createBook(self):
        db = self.conMan.logOn()
        bookCursor = db.cursor()

        print('\nINPUT DATA BUKU\n')
        book_id = input('Id Buku: ')
        book_name = input('Judul Buku: ')
        book_genre = input('Genre Buku: ')
        quantity = input('Jumlah Buku: ')

        query = "INSERT INTO book VALUES('%s', '%s', '%s', %i)" % (book_id, book_name, book_genre, int(quantity))
        bookCursor.execute(query)
        db.commit()

        if bookCursor.rowcount > 0:
            print('Data Berhasil Ditambahkan!!!')

    def updateBook(self, listbook):
        db = self.conMan.logOn()
        bookCursor = db.cursor()
        print('\nUPDATE DATA BUKU\n')
        book_id = input('Masukkan Id Buku yang akan diubah: ')
        dataStatus = False

        for book in listbook:
            if book_id == book.book_id:
                dataStatus = True
                break
            else:
                dataStatus = False

        if not dataStatus:
            print('Data Tidak Ada')
        else:
            print('\nMasukkan Data Buku Baru')
            book_name = input('Judul Buku: ')
            book_genre = input('Genre Buku: ')
            quantity = input('Jumlah Buku: ')

            query = "UPDATE book SET book_name = '%s', book_genre = '%s', quantity = %i WHERE book_id = '%s'" % (
                book_name, book_genre, int(quantity), book_id)
            bookCursor.execute(query)
            db.commit()

            if bookCursor.rowcount > 0:
                print('Data Berhasil Diubah!!!')

    def deleteBook(self, listbook):
        db = self.conMan.logOn()
        bookCursor = db.cursor()

        print('\nDELETE DATA BUKU\n')
        book_id = input('Masukkan Id Buku yang akan dihapus: ')
        dataStatus = False

        for book in listbook:
            if book_id == book.book_id:
                dataStatus = True
                break
            else:
                dataStatus = False

        if not dataStatus:
            print('Data Tidak Ada')
        else:
            query = "DELETE FROM book WHERE book_id = '%s'" % book_id
            bookCursor.execute(query)
            db.commit()

            if bookCursor.rowcount > 0:
                print('Data Berhasil Dihapus!!!')