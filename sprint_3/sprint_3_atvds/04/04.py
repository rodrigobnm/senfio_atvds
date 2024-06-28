# ->> Ex 04) Crie um app que recebe um número inteiro e cria uma matriz, aleatória, através da lib 'numpy' e exiba o resultado.
#    * Utilize ambiente virtual
#    * Guarde os dados do ambiente virtual num arquivo 'requirements.txt'


import numpy

tamanhoMatriz = int(input("Tamanho da matriz: "))
matrix = numpy.random.randint(0, 100, size=(tamanhoMatriz, tamanhoMatriz))
print(matrix)
