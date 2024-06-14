#->> Ex 01) Escreva uma função que solicita que o usuário escreva
# uma palavra e exiba, num dicionário, os caracteres e suas quantidades
# na palavra inserida.
def palavraDicionario(palavra):
    destPalavra = {}
    palavraSplitada = list(palavra)
    for i in palavraSplitada:
        if i not in destPalavra:
            destPalavra[i] = 1
        else:
            destPalavra[i] = destPalavra[i] + 1
    return destPalavra
palavraEntrada = input("Digite uma palavra: ")
print(palavraDicionario(palavraEntrada))