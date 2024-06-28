# ->> Ex 02) Crie um app de notas em terminal, nele você poderá 
# criar uma nota, abrir uma nota, deletar uma nota e editar uma nota. 
# Cada nota é um arquivo txt
# Ao selecionar "Abrir nota" o usuário deve digitar o nome da nota e o programa deve ser 'case-insensitive'.
# Divida as opçẽs do menu em módulos diferentes.
import os

def criarNota():
    nomeArquivo = input("digite o nome do arquivo: ")
    nomeArquivo = nomeArquivo.lower()
    arq = open(nomeArquivo + ".txt", "w")
    valorDaNota = input("Digite Nota: ")
    arq.write(valorDaNota)
    arq.close()

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

def deletarNota():
    nomeArquivo = input("digite o nome do arquivo: ")
    nomeArquivo = nomeArquivo.lower()
    try:
        os.remove(nomeArquivo + ".txt")
    except FileNotFoundError:
        print("Arquivo nao existe")

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


while True:
    operacaoUsuario = int(input("1. Criar Nota\n2. Abrir Nota\n3. Deletar Nota\n4. Editar Nota \n5. Sair\n"))
    if operacaoUsuario == 1:
        criarNota()
    elif operacaoUsuario == 2:
        abrirNota()
    elif operacaoUsuario == 3:
        deletarNota()
    elif operacaoUsuario == 4:
        editarNota()
    elif operacaoUsuario == 5:
        break