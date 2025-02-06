#Faça uma função que, dado um número inteiro n, desenhe um
#triângulo invertido na tela de base n, usando caracteres ’*’.

def triangulo_invertido(n):
    recuo = 0
    while(n>0):
        print(recuo*" ", end = "")
        print(n*"* ")
        n = n-2
        recuo = recuo + 2

