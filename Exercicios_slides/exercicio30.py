#Faça uma função que, dado um número n e um valor v (por
#padrão, valendo 0), cria uma lista de n posições com cada posição
#valendo v. Documente sua função.

def cria_lista_n_valores_v(n,v = 0):
    """Cria uma lista de n posições, cada valendo uma valendo v

    Se n é negativo ou nulo, devolve lista vazia

    Parâmetros:

    n -- número de elementos na lista
    v -- valor de cada elemento na lista
    """
    return [v]*n

