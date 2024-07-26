from Client import Client
from Library import Library

# from funcoes import list_book, lend_book, return_book

clients = {}

while True:
    name = input("Por favor, insira seu nome: ")
    if name not in clients:
        clients[name] = Client(name)
    client = clients[name]
    menu_options = input("1. Listar Livros Disponiveis\n2. Emprestar Um Livro (Especificado Pelo Nome).\n3. Devolver Um Livro (Especificado Pelo Nome).\n4. Sair\n")
    
    if menu_options == "1":
        print(Library.list_books())

    elif menu_options == "2":
        books_name = input("Digite o Titulo do Livro Que Ira Emprestar: ")
        books_author = input("Autor: ")
        cliente = Client(books_name)
        Client.lend_book(books_name, books_name, books_author)
        
    elif menu_options == "3":
        books_name = input("Digite o Titulo do Livro Que Ira Devolver: ")
        for book in Client.__borrowed_books:
            if book._Book__title == books_name:
                if Client.return_book(book):
                    print("Livro devolvido com sucesso!")
                else:
                    print("Você não emprestou este livro!")


    