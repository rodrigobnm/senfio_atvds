from Book import Book
from Client import Client
from Library import Library

library = Library()
client_name = input("Informe o nome do cliente: ")
client = Client(client_name)
library.add_client(client)
    
while True:
    print("1. Listar Livros Disponiveis\n2. Emprestar Um Livro\n3. Devolver Um Livro\n4. Sair\n")
    choice = int(input("Escolha Uma Opcao: "))
        
    if choice == 1:
        print(library.list_books())
        
    elif choice == 2:
        book_title = input("Informe o Titulo Do Livro: ")
        book = None
        for b in library._Library__books:
            if b._Book__title == book_title:
                book = b
            break
        if book:
            if client.lend_book(book):
                print(f"Livro '{book_title}' Emprestado Com Sucesso!")
            else:
                print(f"Livro '{book_title}' Nao Esta disponivel.")
        else:
            print(f"Livro '{book_title}' Nao Encontrado.")
        
    elif choice == 3:
        book_title = input("Informe o Titulo Do Livro: ")
        book = None
        for b in client._Client__borrowed_books:
            if b._Book__title == book_title:
                book = b
            break

        if book:
            if client.return_book(book):
                print(f"Livro '{book_title}'Devolvido Com Sucesso!")
            else:
                print(f"Erro Ao Devolver o Livro '{book_title}'.")
        else:
            print(f"Livro '{book_title}' Nao Encontrado Entre Os Livros Emprestados.")
        
    elif choice == 4:
        break
        
    else:
        print("Opcao Invalida! Tente Novamente.")

