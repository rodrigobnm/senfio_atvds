class Book():
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__available = True
    def loan(self):
        if self.__available is True:
            self.__available = False
            return print(f"Livro, {self.__title}, Emprestado Com Sucesso! ")
        else: 
            return print(f"Livro, {self.__title}, Nao Disponivel")
    def give_back(self):
        self.__available = True
        return print(f"{self.__title}, Marcado Como Disponivel! ")
    def its_available(self):
        return self.__available
    def __str__(self):
        return f"Titulo: {self.__title}\nAutor: {self.__author}\nDisponivel:{self.__available}\n"
