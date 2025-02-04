#Faça um programa que, dado n, imprime um quadrado
#formado por *’s com n linhas e n colunas.

n = int(input("Digite o tamanho do lado do quadrado: "))

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

