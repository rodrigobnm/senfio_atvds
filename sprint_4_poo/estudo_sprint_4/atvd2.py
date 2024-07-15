from classes_da_atvd_2 import Livro

livro1 = Livro("Titulo 1", "Autor 1", 20)
livro1.informacoes()
livro1.leitura(20)

livro2 = Livro("Titulo 2", "Autor 2", 40)
livro2.informacoes()
livro2.leitura(40)

livros = list()
n_livros = 0
while True:
    continuar = input("Digite f para finalizar: ")
    if continuar == "f":
        break
    titulo = input("Titulo: {n_livros} -> ")
    autor = input("Autor: {n_livros} -> ")
    pg = int(input("Paginas: {n_livros} -> "))
    livros.append(Livro(titulo, autor, pg))
    
for i in livros:
    i.informacoes()

    