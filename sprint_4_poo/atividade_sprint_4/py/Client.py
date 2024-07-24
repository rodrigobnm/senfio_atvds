from Book import Book

class Client(Book):
    def __init__(self, name):
        super.__init__(self.__title, self.__author, self.__available)
        self.__name = name
        self.__borrowed_books = [
            Book(self.__title, self.__author, self.__available),
        ]
    def lend_book(self, book):
        for i in self.__title:
            self.__available = False
        return 
    def return_book(self, book):
        for i in self.__title:
            self.__available = True
        return 
    def __str__(self):
        print(f"Cliente: {self.__name}")
        for i in self.__borrowed_books:
            print(f"\n{i}\n")
        return 
