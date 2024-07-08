def criarNota():
    nomeArquivo = input("digite o nome do arquivo: ")
    nomeArquivo = nomeArquivo.lower()
    arq = open(nomeArquivo + ".txt", "w")
    valorDaNota = input("Digite Nota: ")
    arq.write(valorDaNota)
    arq.close()