class Book:
    book_id = ''
    book_name = ''
    book_genre = ''
    quantity = 0

    def __init__(self, book_id, book_name, book_genre, quantity):
        self.book_id = book_id
        self.book_name = book_name
        self.book_genre = book_genre
        self.quantity = quantity
