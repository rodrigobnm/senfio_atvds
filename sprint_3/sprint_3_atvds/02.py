# ->> Ex 02) Crie um app de notas em terminal, nele você poderá 
# criar uma nota, abrir uma nota, deletar uma nota e editar uma nota. 
# Cada nota é um arquivo txt
# Ao selecionar "Abrir nota" o usuário deve digitar o nome da nota e o programa deve ser 'case-insensitive'.
# Divida as opçẽs do menu em módulos diferentes.
import os

def criarNota():
    nomeArquivo = input("digite o nome do arquivo: ")
    nomeArquivo = nomeArquivo.lower()
    arq = open("sprint_3/sprint_3_atvds/notas_atvd_2/" + nomeArquivo + ".txt", "w")
    valorDaNota = input("Digite Nota: ")
    arq.write(valorDaNota)
    arq.close()

def abrirNota():
    nomeArquivo = input("digite o nome do arquivo: ")
    nomeArquivo = nomeArquivo.lower()
    arq = open("sprint_3/sprint_3_atvds/notas_atvd_2/" + nomeArquivo + ".txt", "a")
    return nomeArquivo + ".txt"

def deletarNota():
    nomeArquivo = input("digite o nome do arquivo: ")
    nomeArquivo = nomeArquivo.lower()
    os.remove("sprint_3/sprint_3_atvds/notas_atvd_2/" + nomeArquivo + ".txt")

def editarNota():
    nomeArquivo = input("digite o nome do arquivo: ")
    nomeArquivo = nomeArquivo.lower()
    arq = open("sprint_3/sprint_3_atvds/notas_atvd_2/" + nomeArquivo + ".txt", "r+")
    print(arq.read())
    adicaoNota = input("Digite a adicao para sua nota: ")
    adicaoNota = "\n" + adicaoNota
    arq.write(adicaoNota)
    arq.close()


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