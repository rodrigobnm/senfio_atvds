# ->> Ex 05) Crie um app de agenda telefônica, este deve usar a lib 'prettytable' para exibir os dados da agenda. 
#        O menu terá as opçẽs: Add, listar e buscar contato, além de uma opção de sair do sistema.
#        * Os contatos devem ser salvos num arquivo txt para manter a persistência do sistema.
#        * Crie o menu e as opções do menu em módulos diferentes. Cada ação em seu devido módulo. 
#        * Trate possíveis erros 
#        * Os contatos têm nome, número e email
#        * Utilize ambiente virtual
#        * Guarde os dados do ambiente virtual num arquivo 'requirements.txt'

from prettytable import PrettyTable
import add
import listar
import buscar 

tabela_contatos = PrettyTable()
tabela_contatos.field_names = ["Contatos", "Nomes", "Numeros", "Emails"]

while True:
    acao = int(input("Digite acao que deseja:\n1. Adicionar contato \n2. Listar Contato\n3. Buscar Contato\n4. Sair\n"))
    if acao == 1:
        add.add_contato(tabela_contatos)
    elif acao == 2:
        listar.listar_contato(tabela_contatos)
    elif acao == 3:
        buscar.buscar_contato()
    elif acao == 4:
        break
    else:
        print("Opcao invalida! Tente Novamente. ")