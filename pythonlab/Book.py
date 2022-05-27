from Publication import Publication


class Book(Publication):
    def __init__(self, name: str, price: float, author: str, book_type: str):
        super().__init__(name, price)
        self.author = author
        self.book_type = book_type

    def __str__(self):
        return f"Book - " + super(Book, self).__str__() \
               + f", Author: {self.author}, Book type: {self.book_type}"
