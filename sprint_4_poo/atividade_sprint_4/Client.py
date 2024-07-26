from Book import Book

class Client():
    def __init__(self, name):
        self.__name = name
        self.__borrowed_books = []
    def lend_book(self, book, author):
        title = book
        x = Book(title, author)
        if x.loan():
            return True
        self.__borrowed_books.append(title)
        return False
    def return_book(self, book):
        if book in self.__borrowed_books:
            book.give_back()
            self.__borrowed_books.remove(book)
            return True
        return False 
    def __str__(self):
        borrowed_books_str = ", ".join([str(book) for book in self.__borrowed_books])
        return f"Cliente: {self.__name}, Livros Emprestados: [{borrowed_books_str}]"

