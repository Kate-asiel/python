class Publication:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}"


class Book(Publication):
    def __init__(self, name: str, price: float, author: str, book_type: str):
        super().__init__(name, price)
        self.author = author
        self.book_type = book_type

    def __str__(self):
        return f"Book - {super().__str__()}, Author: {self.author}, Book type: {self.book_type}"


class Monograph(Publication):
    def __init__(self, name: str, price: float, topic: str, count_of_pages: int):
        super().__init__(name, price)
        self.count_of_pages = count_of_pages
        self.topic = topic

    def __str__(self):
       return f"Monograph - {super().__str__()}, Count of pages: {self.count_of_pages}, Topic: {self.topic}"

class Magazine(Publication):
    def __init__(self, name: str, price: float, publisher: str, circulation: int):
        super().__init__(name, price)
        self.publisher = publisher
        self.circulation = circulation

    def __str__(self):
         return f"Magazine - {super().__str__()}, Publisher: {self.publisher}, Circulation: {self.circulation}"
