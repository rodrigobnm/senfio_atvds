def abrirNota():
    nomeArquivo = input("digite o nome do arquivo: ")
    nomeArquivo = nomeArquivo.lower()
    try:
        arq = open(nomeArquivo + ".txt", "r")
    except FileNotFoundError:
        print("Arquivo Nao encontrado\nRedirecionando para criacao: ")
    else:
        print("Conteúdo atual da nota:\n")
        print(arq.read())