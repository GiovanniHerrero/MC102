#Imprima os n primeiros números naturais em ordem inversa.

n = int(input("Quantos inteiros deseja digitar?"))
lista = list()
for i in range(n):
    inteiro = int(input("Digite o próximo inteiro da lista"))
    lista.append(inteiro)
