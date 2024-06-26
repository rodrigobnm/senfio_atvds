
# ->> Ex 01) Escreva uma função que recebe 2 números, divide-os e retorne o resultado.
#  Caso ocorra algum erro, explique o que aconteceu. 
#  Caso o resultado seja inteiro, apresente-o como tal, caso seja float, apresente-o com 2 casas decimais. **

def divisao():
    try:
        valor1 = float(input("Valor 1:"))
        valor2 = float(input("Valor 2:"))
        divisao = valor1 / valor2
        if valor1 % valor2 == 0:
            print(int(divisao))
        else:
            print(f'{(divisao):.2f}')
    except ValueError:
        print("Nao e possivel fazer a divisao por nao numeros\nTente novamente")
    except ZeroDivisionError:
        print("Nao e possivel fazer a divisao por 0\nTente novamente")
    except:
        print("Erro encontrado\nTente novamente")

while True:
    divisao()