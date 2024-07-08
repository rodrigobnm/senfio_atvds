def editarNota():
    nomeArquivo = input("digite o nome do arquivo: ")
    nomeArquivo = nomeArquivo.lower()
    try:
        arq = open(nomeArquivo + ".txt", "r+")
    except FileNotFoundError:
        print("Arquivo nao existe")
    else:
        print("Conteúdo atual da nota:\n")
        print(arq.read())
        adicaoNota = input("\nDigite a adição para sua nota: ")
        arq.write("\n" + adicaoNota)
        print("Nota editada com sucesso.")
