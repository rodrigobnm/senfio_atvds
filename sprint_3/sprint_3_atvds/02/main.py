# ->> Ex 02) Crie um app de notas em terminal, nele você poderá 
# criar uma nota, abrir uma nota, deletar uma nota e editar uma nota. 
# Cada nota é um arquivo txt
# Ao selecionar "Abrir nota" o usuário deve digitar o nome da nota e o programa deve ser 'case-insensitive'.
# Divida as opçẽs do menu em módulos diferentes.
import criar
import abrir
import deletar
import editar

while True:
    try:
        operacaoUsuario = int(input("1. Criar Nota\n2. Abrir Nota\n3. Deletar Nota\n4. Editar Nota \n5. Sair\n"))
        if operacaoUsuario == 1:
            criar.criarNota()
        elif operacaoUsuario == 2:
            abrir.abrirNota()
        elif operacaoUsuario == 3:
            deletar.deletarNota()
        elif operacaoUsuario == 4:
            editar.editarNota()
        elif operacaoUsuario == 5:
            break
        else:
            print("Digite um Numero Valido")
    except ValueError:
        print("Digite um Numero! ")