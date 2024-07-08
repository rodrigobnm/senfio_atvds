def add_contato(tabela_contatos):
    arq = open("contatos.txt", "a")
    nome = input("Digite o Nome: ")
    contato = input("Digite o Contato: ")
    numero = input("Digite o Numero: ")
    email = input("Digite o Email: ")
    tabela_contatos.add_row([contato, nome, numero, email])
    arq.write(f"{contato}, Nome: {nome}, Numero: {numero}, Email: {email}\n")