#Faça uma função que recebe uma lista e devolve uma nova
#lista invertida.

def inverte_lista(lista):
    for i in range(len(lista)//2):
        lista[i],lista[len(lista) - 1 -i] = lista[len(lista) -1 -i], lista[i]
    return lista

print(inverte_lista([1,2,3,4,5,6,7,8,9,10,11]))
