#->> Ex 05) Você está desenvolvendo um sistema simples de gerenciamento de alunos para uma escola.
# Este sistema deve ser capaz de armazenar e manipular informações dos alunos, incluindo suas notas.
# Você deve implementar as seguintes funcionalidades:

    #   Entrada de Dados:
        #- Permitir que o usuário insira o nome de um aluno.
        #    * Os nomes dos alunos devem ser únicos.
        #- Permitir que o usuário insira as notas do aluno em 5 matérias escolares: Português, Matemática, Ciências, Geografia e História.

    #   Processamento de Dados:
        #- Calcular a média das notas para cada aluno.
        #- Verificar se o aluno passou ou não (média maior ou igual a 7).

    #   Relatório:
        #- Exibir um relatório com o nome do aluno, as notas em cada matéria, a média das notas e se o aluno passou ou não.

    #   Manipulação de Dados:
        #- Permitir que o usuário adicione novos alunos e notas.
        #- Permitir que o usuário remova alunos.
        #- Permitir que o usuário veja a lista de todos os alunos.

    # *** Ao inicar o programa o usuário deve escolher num menu a opção desejada e o sistema deve executar até que o usuário insira um comando de parada.

notas = dict()
def adicionarAluno(aluno):
    if aluno not in notas:
        port = float(input("Nota de Portugues: "))
        mat = float(input("Nota de Matematica: "))
        cienc = float(input("Nota de Ciencias: "))
        geo = float(input("Nota de Geografia: "))
        hist = float(input("Nota de Historia: "))
        notas[aluno] = [port, mat, cienc, geo, hist]
    else:
        cond = input(f"Deseja reescrever as notas de {aluno}? (s/n)  ")
        if cond == "s":
            deletar(aluno)
            adicionarAluno(aluno)

def processamentoDados(aluno):
    if aluno in notas:
        somaNotas = 0
        passou = False
        for valor in notas.get(aluno, []):
            somaNotas += valor
        if somaNotas / 5 >= 7:
            passou = True
            print(f"{aluno} passou!")
        else:
            print(f"{aluno} nao passou")
        print(f"Media de {aluno} é {somaNotas / 5}")
    else:
        print("Usuario nao encontrado")
        return
    return passou, somaNotas / 5

def relatorio(aluno):
    if aluno in notas:
        passou, mediaFinal = processamentoDados(aluno)
        print(f"Notas:\nPortugues: {notas.get(aluno, [])[0]}\nMatematica {notas.get(aluno, [])[1]}\nCiencias {notas.get(aluno, [])[2]}\n"
              f"Geografia {notas.get(aluno, [])[3]}\nHistoria {notas.get(aluno, [])[4]}\n")
    else:
        print("aluno nao encontrado")

def deletar(aluno):
    if aluno in notas:
        print(f"dados de {aluno} foram deletadas")
        del notas[aluno]
    else:
        print("usuario nao encontrado")

while True:
    nome = input("Digite o nome do aluno: ")
    processo = int(input("Escolha uma opção:\n1.Entrada de Dados\n2.Processamento de Dados\n3.Relatorio\n4.Deletar Aluno\n5.Sair\n"))
    if processo == 1:
        adicionarAluno(nome)
    elif processo == 2:
        processamentoDados(nome)
    elif processo == 3:
        relatorio(nome)
    elif processo == 4:
        deletar(nome)
    elif processo == 5:
        break
    else:
        print("Digite um processo valido! ")