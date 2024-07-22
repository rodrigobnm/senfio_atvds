from Book import Book
from Client import Client
from Library import Library

from funcoes import list_book, lend_book, return_book

from tabulate import tabulate

while True:
    username = input("Nome: ")
    menu_options = input("1. Listar Livros Disponiveis\n2. Emprestar Um Livro (Especificado Pelo Nome).\n3. Devolver Um Livro (Especificado Pelo Nome).\n4. Sair\n")
    if menu_options == "1":
        list_book()
    elif menu_options == "2":
        books_name = input("Digite o Nome do Livro: ")
        lend_book(books_name)
    elif menu_options == "3":
        books_name = input("Digite o Nome do Livro: ")
        return_book(books_name)
    elif menu_options == "4": 
        break
    else: 
        print("Digite um numero das opcoes! ")


    