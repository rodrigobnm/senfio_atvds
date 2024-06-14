# ->> Ex 03) Crie um programa que pede ao usuário vários
# números e quando o usuário inserir a palavra "FIM",
# o programa deve exibir, sem repetir, todos os números inseridos.
setNum = set()
checkFim = "1"
while checkFim != "FIM":
    checkFim = input("Digite um numero ou FIM para sair: ")
    if checkFim != "FIM":
        setNum.add(checkFim)

print(setNum)


