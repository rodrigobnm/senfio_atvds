from Book import Book
from Client import Client
from Library import Library

from tabulate import tabulate

def list_book():
    return
def lend_book(books_name):
    author = input("Digite o Nome Do Autor: ")
    lend_book = Book(books_name, author)
    lend_book.loan()
    return 
def return_book(books_name):
    author = input("Digite o Nome Do Autor: ")
    lend_book = Book(books_name, author)
    lend_book.give_back()
    return