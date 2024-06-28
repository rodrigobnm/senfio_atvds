from prettytable import PrettyTable

# Criando uma tabela de exemplo
table = PrettyTable()
table.field_names = ["Nome", "Idade", "Profissão"]

# Adicionando algumas linhas
table.add_row(["Ana", 25, "Engenheira"])
table.add_row(["Bruno", 30, "Médico"])
table.add_row(["Carla", 28, "Professora"])

# Função para buscar um nome em uma linha específica
def buscar_nome_em_linha(tabela, nome, linha):
    try:
        # Obtendo a linha especificada
        row = tabela._rows[linha]
        # Verificando se o nome está presente na linha
        if nome in row:
            return f"Nome '{nome}' encontrado na linha {linha}: {row}"
        else:
            return f"Nome '{nome}' não encontrado na linha {linha}."
    except IndexError:
        return f"Linha {linha} não existe na tabela."

for x in tabela


















# Exemplo de uso da função
linha_especifica = 1  # Índice da linha que você deseja verificar (0 baseado)
nome_procurado = "Bruno"

resultado = buscar_nome_em_linha(table, nome_procurado, linha_especifica)
print(resultado)
