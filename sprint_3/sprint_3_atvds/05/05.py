from prettytable import PrettyTable

def adicionar_contato():
    nome = input("Nome: ")
    numero = input("Número: ")
    email = input("Email: ")
    with open("contatos.txt", "a") as f:
        f.write(f"{nome},{numero},{email}\n")
    print("Contato adicionado com sucesso!")

def listar_contatos():
    table = PrettyTable(["Nome", "Número", "Email"])
    try:
        with open("contatos.txt", "r") as f:
            for linha in f:
                nome, numero, email = linha.strip().split(",")
                table.add_row([nome, numero, email])
        print(table)
    except FileNotFoundError:
        print("Nenhum contato encontrado.")

def buscar_contato():
    busca = input("Digite o nome para buscar: ").lower()
    table = PrettyTable(["Nome", "Número", "Email"])
    encontrado = False
    try:
        with open("contatos.txt", "r") as f:
            for linha in f:
                nome, numero, email = linha.strip().split(",")
                if busca in nome.lower():
                    table.add_row([nome, numero, email])
                    encontrado = True
        if encontrado:
            print(table)
        else:
            print("Contato não encontrado.")
    except FileNotFoundError:
        print("Nenhum contato encontrado.")

def main():
    while True:
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Buscar Contato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

# 05\Scripts\activate
# pip install prettytable
# pip freeze > requirements.txt
# python 05.py
