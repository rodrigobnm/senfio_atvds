class Client:
    def __init__(self, name):
        self.__name = name
        self.__borrowed_books = []
    
    def lend_book(self, book):
        if book.loan():
            self.__borrowed_books.append(book)
            return True
        return False
    
    def return_book(self, book):
        if book in self.__borrowed_books:
            book.give_back()
            self.__borrowed_books.remove(book)
            return True
        return False
    
    def __str__(self):
        borrowed_books_titles = [book.__str__() for book in self.__borrowed_books]
        return f"Cliente: {self.__name}, Emprestado: {borrowed_books_titles}"
