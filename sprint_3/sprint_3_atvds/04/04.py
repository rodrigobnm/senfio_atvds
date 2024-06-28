import numpy as np

def main():
    n = int(input("Digite um número inteiro para o tamanho da matriz: "))
    matrix = np.random.randint(0, 100, size=(n, n))
    print("Matriz aleatória:")
    print(matrix)

if __name__ == "__main__":
    main()


# 04\Scripts\activate
# pip install numpy
# pip freeze > requirements.txt
# python 04.py