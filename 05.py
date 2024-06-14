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

alunos = set()
notas = dict()
def adicionar_aluno(aluno):
    alunos.add(aluno)
    port = float(input("Nota de Portugues: "))
    mat = float(input("Nota de Matematica: "))
    cienc = float(input("Nota de Ciencias: "))
    geo = float(input("Nota de Geografia: "))
    hist = float(input("Nota de Historia: "))

