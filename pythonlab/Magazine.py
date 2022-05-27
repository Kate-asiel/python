from Publication import Publication


class Magazine(Publication):
    def __init__(self, name: str, price: float, publisher: str, circulation: int):
        super().__init__(name, price)
        self.publisher = publisher
        self.circulation = circulation

    def __str__(self):
        return f"Magazine - " + super(Magazine, self).__str__() \
               + f", Publisher: {self.publisher}, Circulation: {self.circulation}"
