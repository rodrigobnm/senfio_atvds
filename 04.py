#->> Ex 04) Escreva um programa que receba 2
# listas de valores inteiros, e ao fim exiba a
# intersecção delas.
# ** O usuário deve inserir valores para a primeira
# lista e ao digitar 'FIM' passe para a segunda lista
# ao digitar 'FIM' novamente a função seja executada.

interseccao = []
l1 = []
x = 0
y = 0
l2 = []

while x != "FIM":
   x = input("digite valores da lista 1 ou FIM: ")
   if x != "FIM": #evitando o erro da ultima rodagem do while n conseguir identificar o FIM como um int (ate pq ele n eh)
       l1.append(int(x))

while y != "FIM":
   y = input("digite valores da lista 2 ou FIM: ")
   if y != "FIM": #evitando o erro da ultima rodagem do while n conseguir identificar o FIM como um int (ate pq ele n eh)
       l2.append(int(y))


for item1 in l1:
   if item1 in l2 and item1 not in interseccao:
       interseccao.append(item1)


print(f"\n\n{interseccao}")
