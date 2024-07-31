class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__available = True
    
    def loan(self):
        if self.__available:
            self.__available = False
            return True
        return False
    
    def give_back(self):
        self.__available = True
    
    def its_available(self):
        return self.__available
    
    def __str__(self):
        return f"Titulo: {self.__title}, Autor: {self.__author}, Disponibilidade: {self.__available}"
