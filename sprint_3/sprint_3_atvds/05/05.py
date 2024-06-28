# ->> Ex 05) Crie um app de agenda telefônica, este deve usar a lib 'prettytable' para exibir os dados da agenda. 
#        O menu terá as opçẽs: Add, listar e buscar contato, além de uma opção de sair do sistema.
#        * Os contatos devem ser salvos num arquivo txt para manter a persistência do sistema.
#        * Crie o menu e as opções do menu em módulos diferentes. Cada ação em seu devido módulo. 
#        * Trate possíveis erros 
#        * Os contatos têm nome, número e email
#        * Utilize ambiente virtual
#        * Guarde os dados do ambiente virtual num arquivo 'requirements.txt'

from prettytable import PrettyTable

def add_contato():
    arq = open("contatos.txt", "w")
    nome = input("Digite o Nome: ")
    contato = input("Digite o Contato: ")
    numero = input("Digite o Numero: ")
    email = input("Digite o Email: ")
    tabela_contatos.add_row([contato, nome, numero, email])
    arq.write(f"Contato: {contato}, Nome: {nome}, Numero: {numero}, Email: {email}\n")

def listar_contato():
    print(tabela_contatos.get_string(fields=["Contatos"]))

def buscar_contato():
    nome_buscar = input("Digite Contato Para Buscar: ")
    tabela_contatos_splitada = tabela_contatos.get_string().split(" ")
    bool = 0
    for i in tabela_contatos_splitada:
        if i != " " and i != "|" and i != "\n":
            if i == nome_buscar:
                nome_buscar = False
                bool = 1
            if bool != 0:
                bool += 1
                if bool == 2:
                    print(f"\nContato: {i}")
                elif bool == 7:
                    print(f"Nome: {i}")
                elif bool == 11:
                    print(f"Numero: {i}")
                elif bool == 15:
                    print(f"Email: {i}\n")
                elif bool == 16:
                    bool = 0

tabela_contatos = PrettyTable()
tabela_contatos.field_names = ["Contatos", "Nomes", "Numeros", "Emails"]

while True:
    acao = int(input("Digite acao que deseja:\n1. Adicionar contato \n2. Listar Contato\n3. Buscar Contato\n4. Sair\n"))
    if acao == 1:
        add_contato()
    elif acao == 2:
        listar_contato()
    elif acao == 3:
        buscar_contato()
    elif acao == 4:
        break
    else:
        print("Opcao invalida! Tente Novamente. ")