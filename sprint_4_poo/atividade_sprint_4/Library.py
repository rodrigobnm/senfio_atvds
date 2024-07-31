from tabulate import tabulate

class Library:
    def __init__(self):
        self.__books = []
        self.__clients = []
    
    def add_book(self, book):
        self.__books.append(book)
    
    def add_client(self, client):
        self.__clients.append(client)
    
    def list_books(self):
        books_info = [[book._Book__title, book._Book__author, book._Book__available] for book in self.__books]
        return tabulate(books_info, headers=["Titulo", "Autor", "Disponibilidade"], tablefmt="grid")
    
    def __str__(self):
        return self.list_books()
