#Dada uma sequência de números reais S, um valor é um mínimo local, se os
#dois adjacentes a ele forem maiores (isto é, si−1 > si < si+1 ). Faça um
#programa que leia uma sequência de inteiros S e imprima as posições dos
#mínimos locais nela.

n = int(input("Entre com o número de elementos na lista: "))
lista = list()

for i in range(n):
    numero = int(input("Entre com o próximo número na lista: "))
    lista.append(numero)

#Imprimimos i+1, pois as posições na sequência começam em 1
for i in range(n):
    if i == 0:
        if lista[0]<lista[1]:
            print(i+1)
    elif i == n-1:
        if lista[n-1]<lista[n-2]:
            print(i+1)
    else:
        if lista[i]<lista[i-1] and lista[i]<lista[i+1]:
            print(i+1)