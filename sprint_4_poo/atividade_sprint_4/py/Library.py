from Book import Book
from Client import Client

from tabulate import tabulate

class Library(Book, Client):
    def __init__(self):
        super.__init__(self.__title, self.__name)
        self.__books = list()
        self.__books.append(self.__title)
        self.__clients = list()
        self.__clients.append(self.__name)
    def add_book(self, book):
        self.__books.append(book)
        return 
    def add_client(self, client):
        self.__clients.append(client)
        return
    def list_books(self):
        ## tabulate 
        return 
    def __str__(self):
        # retorna lista de livros formatada como uma string
        return
