import datetime as dt

class Transaction:
    today = dt.date.today()

    transaction_id = ''
    user_id = ''
    book_id = ''
    borrow_date = today.strftime("%Y-%m-%d")
    return_date = today + dt.timedelta(days=7)

    def __init__(self, transaction_id, user_id, book_id):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.book_id = book_id
