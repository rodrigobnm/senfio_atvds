def listar_contato(tabela_contatos):
    try:
        with open("contatos.txt", 'r') as arquivo:
            for linha in arquivo:
                print("Contato: ", linha.strip())
    except FileNotFoundError:
        print("Arquivo não encontrado.")