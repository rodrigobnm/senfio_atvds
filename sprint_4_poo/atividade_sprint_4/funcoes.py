from Client import Client
from Library import Library

def list_book():
    print(Library.list_books())
    return
def lend_book(books_name):
    if Client.lend_book(books_name):
        print("Livro Emprestado Com Sucesso!")
    else:
        print("Livro Nao Disponível!")
        
def return_book(books_name):
    for book in Client.__borrowed_books:
        if book._Book__title == books_name:
            if Client.return_book(book):
                print("Livro devolvido com sucesso!")
            break
    else:
        print("Você não emprestou este livro!")
    return