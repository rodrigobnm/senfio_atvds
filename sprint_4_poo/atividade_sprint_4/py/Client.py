from Book import Book

from tabulate import tabulate

class Client(Book):
    def __init__(self, name):
        super.__init__(self.__title, self.__author, self.__available)
        self.__name = name
        self.__borrowed_books
    def lend_book(self, book):
        return 
    def return_book(self, book):
        return 
    def __str__(self):
        return
