#Faça uma função que recebe uma lista e devolve uma nova
#lista invertida.

def inverte_lista(lista):
    for i in range(len(lista)//2):
        lista[i],lista[len(lista) - 1 -i] = lista[len(lista) -1 -i], lista[i]
    return lista

