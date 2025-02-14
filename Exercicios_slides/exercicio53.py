#Faça uma função que, dada uma lista, devolve uma nova lista
#sem elementos repetidos. Dica: use conjuntos!

def lista_sem_repeticao(lista):
    """Devolve uma lista sem elementos repetidos a partir de lista passada como parâmetro

    Argumentos:
    lista -- A lista cujos elementos serão adicionados na nova lista (sem repetição)
    """
    nova_lista = list()
    conjunto = set()

    for elemento in lista:
        conjunto.add(elemento)

    for elemento in conjunto:
        nova_lista.append(elemento)
    return nova_lista