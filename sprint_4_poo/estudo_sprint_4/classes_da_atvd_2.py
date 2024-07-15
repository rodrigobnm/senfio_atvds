class Livro():
    def __init__(self, titulo, autor, num_pgs):
        self.titulo = titulo
        self.autor =  autor
        self.num_pgs = num_pgs

    def informacoes(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nPaginas: {self.num_pgs}\n"
        
    def leitura(self, pgs_para_ler):
        if pgs_para_ler > self.num_pgs:
            pgs = 1
            while pgs <= self.num_pgs:
                print(f"Pagina {pgs}: --conteudo--")
                pgs += 1
            print(f"Ha {pgs_para_ler - self.num_pgs} pagina(s) nao existentes! ")
        else:
            pgs = 1
            while pgs <= pgs_para_ler:
                print(f"Pagina {pgs}: --conteudo--")
                pgs += 1
    def buscar_livros(self, titulo):
           if self.titulo == titulo:
               return True
    def listar_livros(self):
        print(self.autor)

class colecao_de_livros(Livro):
    def __init__(self, titulo, autor, num_pgs, quantidade, versao):
        super.__init__(titulo, autor, num_pgs)
        self.quantidade = quantidade
        self.versao = versao
    def entrada_de_sub_nomes(self):
        controle = 1
        dicionario_dos_livros = dict()
        while controle <= self.quantidade:
            sub_nome = input(f"Digite o subnome do livro {self.titulo}: ")
            dicionario_dos_livros.update({f'{self.titulo}: {sub_nome}': controle})
            controle += 1