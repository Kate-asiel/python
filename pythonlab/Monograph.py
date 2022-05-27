from Publication import Publication


class Monograph(Publication):
    def __init__(self, name: str, price: float, topic: str, count_of_pages: int):
        super().__init__(name, price)
        self.count_of_pages = count_of_pages
        self.topic = topic

    def __str__(self):
        return f"Monograph - " + super(Monograph, self).__str__() \
               + f", Count of pages: {self.count_of_pages}, Topic: {self.topic}"
