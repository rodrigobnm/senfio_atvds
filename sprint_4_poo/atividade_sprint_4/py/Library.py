from Book import Book
from Client import Client

from tabulate import tabulate

class Library():
    def __init__(self):
        self.__books = list()
        self.__clients = list()
    def add_book(self, book):
        self.__books.append(book)
        return 
    def add_client(self, client):
        self.__clients.append(client)
        return
    def list_books(self):
        book_data = [[book._Book__title, book._Book__author, book._Book__available] for book in self.__books]
        return tabulate(book_data, headers=['Título', 'Autor', 'Disponível']) 
    def __str__(self):
        return self.list_books()