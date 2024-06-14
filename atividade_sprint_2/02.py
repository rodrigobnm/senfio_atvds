# ->> Ex 02) Dada uma lista de valores inteiros, crie uma função que retorne
# a soma dos valores pares da lista.
def somaPares(lista):
   soma = 0
   for num in lista:
       if num % 2 == 0:
           soma += num
   return soma


listaExemplo = [3 ,9, 12, 10]
print(f"somas dos pares: {somaPares(listaExemplo)}")


