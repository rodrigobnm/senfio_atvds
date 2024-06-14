# ->> Ex 03) Crie um programa que pede ao usuário vários
# números e quando o usuário inserir a palavra "FIM",
# o programa deve exibir, sem repetir, todos os números inseridos.
listaNum = []
checkFim = "1"
while checkFim != "FIM":
   tem = False
   checkFim = input("Digite um numero ou FIM para sair: ")
   if checkFim == "FIM":
       print(listaNum)
       break
   for n in listaNum:
       if n == checkFim:
           tem = True
           break
   if tem == False:
       listaNum.append(checkFim)
