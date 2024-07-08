def buscar_contato():
    nome_buscado = input("Digite o Nome Buscado: ").lower()
    encontrado = False
    try:
        with open("contatos.txt", 'r') as arquivo:
            for linha in arquivo:
                if nome_buscado.lower() in linha.lower():
                    print("Contato: ", linha.strip())
                    encontrado = True
        if not encontrado:
            print("Nome não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")