#Faça uma função que, dada uma lista l e um valor v (por padrão,
#valendo 0), modifica todas as entradas da lista para v. Documente
#sua função.

def modifica_valores_lista(lista, v = 0):
    """Modifica todas as entrada de da lista para o valor v (padrao = 0)
    
        Parâmetros:

        lista --A lista cujos valores desejamos modificar
        v -- o novo valor de cada entrada na lista (0 por padrão)
    """
    for elemento in lista:
        elemento = v
    return lista
