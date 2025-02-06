#Dois números são amigáveis se pelo menos um deles for igual à
#soma dos divisores próprios do outro.

#Faça uma função que, dados dois números m e n, decide se são
#amigáveis.

def soma_divisores_proprios(x):
    soma = 0
    for i in range(1,(x//2) + 1):
        if x%i == 0:
            soma +=i
    return soma

def sao_amigaveis(x,y):
    s_x = soma_divisores_proprios(x)
    s_y = soma_divisores_proprios(y)
    
    return (y == s_x or x == s_y)

