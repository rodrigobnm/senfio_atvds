import os

def deletarNota():
    nomeArquivo = input("digite o nome do arquivo: ")
    nomeArquivo = nomeArquivo.lower()
    try:
        os.remove(nomeArquivo + ".txt")
    except FileNotFoundError:
        print("Arquivo nao existe")