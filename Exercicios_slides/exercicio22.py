#Faça um programa que, dado n, imprime um quadrado
#formado por *’s com n linhas e n colunas.
#Faça o mesmo para retângulos e para triângulo retângulo isósceles

opcao = int(input(
    "Qual figura deseja desenhar? "
    "Digite 1 para quadrado, "
    "2 para retângulo "
    "e 3 para triângulo retângulo isósceles: "
))     

if opcao == 1:

    n = int(input("Digite o tamanho do lado do quadrado: "))
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()

elif opcao == 2:

    l = int(input("Digite a largura do retângulo: "))
    h = int(input("Digite a altura do retângulo: "))
    for i in range(h):
        for j in range(l):
            print("*", end="")
        print()

else:

    n = int(input("Digite o tamanho do lado do triângulo: "))
    for i in range(1, n+1):
        print(i*"*", end ="")
        print()


