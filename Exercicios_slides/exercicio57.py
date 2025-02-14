#Faça uma função que recebe um conjunto de números e retorna o maior
#produto entre dois números do conjunto

def maior_produto(conjunto):
    """Retorna o maior produto entre dois números do conjunto
    
    Parâmetros:
    conjunto(set)
    """
    lista = list(conjunto)
    produto = lista[0]*lista[1]

    for elemento1 in lista:
        for elemento2 in lista:
            if elemento1 != elemento2 and elemento1*elemento2 > produto:
                produto = elemento1 * elemento2
    return produto

