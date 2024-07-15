from classes_da_atvd_2 import Livro

# livro1 = Livro("Titulo 1", "Autor 1", 20)
# livro1.informacoes()
# livro1.leitura(20)
# 
# livro2 = Livro("Titulo 2", "Autor 2", 40)
# livro2.informacoes()
# livro2.leitura(40)

livros = list()
while True:
    continuar = input("1. Ver Livros\n2. Adicionar Livros\n3. Finalizar Aplicacao\n4. Buscar Livros\n5. Salvar\n")
    if continuar == "1":
        for i in livros:
            print(i.informacoes())
    elif continuar == "2":
        titulo = input(f"Titulo -> ")
        autor = input(f"Autor -> ")
        pg = int(input(f"Paginas -> "))
        livros.append(Livro(titulo, autor, pg))
    elif continuar == "3":
        break
    elif continuar == "4": 
        buscador = input("Digite o titulo: ")
        for i in livros:
            autor = i.buscar_livros(buscador)
            if autor == True:
                print(i.informacoes())
                ler = input("Deseja ler o livro (s/n)?")
                if ler == "s":
                    paginas = int(input("Deseja ler quantas paginas? "))
                    i.leitura(paginas)
    elif continuar == "5":
        arq = open("backup.txt", "w")
        for i in livros:
            arq.write(str(i.informacoes()))
        arq.close()
    else: 
        print("Digite um numero das opcoes! ")


    