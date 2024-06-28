# ->> Ex 04) Crie um app que recebe um número inteiro e cria uma matriz, aleatória, através da lib 'numpy' e exiba o resultado.
#    * Utilize ambiente virtual
#    * Guarde os dados do ambiente virtual num arquivo 'requirements.txt'


import numpy as np

n = int(input("Tamanho da matriz: "))
matrix = np.random.randint(0, 100, size=(n, n))
print("Matriz aleatória:")
print(matrix)

# 04\Scripts\activate
# pip install numpy
# pip freeze > requirements.txt
# python 04.py