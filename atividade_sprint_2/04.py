#->> Ex 04) Escreva um programa que receba 2
# listas de valores inteiros, e ao fim exiba a
# intersecção delas.
# ** O usuário deve inserir valores para a primeira
# lista e ao digitar 'FIM' passe para a segunda lista
# ao digitar 'FIM' novamente a função seja executada.

l1 = set()
x = 0
y = 0
l2 = set()

while x != "FIM":
   x = input("digite valores da lista 1 ou FIM: ")
   if x != "FIM":
       l1.add(int(x))

while y != "FIM":
   y = input("digite valores da lista 2 ou FIM: ")
   if y != "FIM":
       l2.add(int(y))

#transformando as listas em sets e printando a intersecção
print(l1 & l2)