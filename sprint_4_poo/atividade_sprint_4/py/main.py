from Client import Client

from funcoes import list_book, lend_book, return_book

from tabulate import tabulate

clients = {}

while True:
    name = input("Por favor, insira seu nome: ")
    if name not in clients:
        clients[name] = Client(name)
    client = clients[name]
    username = input("Nome: ")
    menu_options = input("1. Listar Livros Disponiveis\n2. Emprestar Um Livro (Especificado Pelo Nome).\n3. Devolver Um Livro (Especificado Pelo Nome).\n4. Sair\n")
    if menu_options == "1":
        list_book()
    elif menu_options == "2":
        books_name = input("Digite o Titulo do Livro Que Ira Emprestar: ")
        lend_book(books_name)
    elif menu_options == "3":
        books_name = input("Digite o Titulo do Livro Que Ira Devolver: ")
        return_book(books_name)
    elif menu_options == "4": 
        break
    else: 
        print("Digite um numero das opcoes! ")


    