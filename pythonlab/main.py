from Book import Book
from Monograph import Monograph
from Magazine import Magazine


def main():
    book = Book("Fifty shades of grey", 80.95, "E. L. James", "Print (hardcover, paperback)")
    monograph = Monograph("Crusades in Palestine", 20.99, "church propaganda", 220)
    magazine = Magazine("Reader's Digest", 100.99, "Reader's Digest Association", 13000000)

    print(book)
    print(monograph)
    print(magazine)


if __name__ == '__main__':
    main()
