#Faça um programa que encontre o mínimo e o máximo em um dado
#conjunto de números.

def min_max_set(conjunto):
    """Devolve uma tupla (a,b) sendo a o menor elemento e b o maior elemento do conjunto
    
    Parâmetros:
    conjunto --o conjunto a ser analisado
    """
    lista_do_conjunto = list(conjunto)
    minimo = lista_do_conjunto[0]
    maximo = lista_do_conjunto[0]

    for i in range(1, len(lista_do_conjunto)):
        if lista_do_conjunto[i] < minimo:
            minimo = lista_do_conjunto[i]
        if lista_do_conjunto[i] > maximo:
            maximo = lista_do_conjunto[i]

    return minimo, maximo

