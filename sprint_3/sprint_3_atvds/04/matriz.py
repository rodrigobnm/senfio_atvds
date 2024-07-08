import numpy

def fazer_matriz(tamanhoMatriz):
    matrix = numpy.random.randint(0, 100, size=(tamanhoMatriz, tamanhoMatriz))
    print(matrix)