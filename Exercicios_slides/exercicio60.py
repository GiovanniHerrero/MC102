#Faça uma função que recebe um conjunto de strings e retorna o maior
#prefixo de todas as strings do conjunto.

def maior_prefixo(conjunto):
    """Dado um conjunto de strings, a função retorna o maior prefixo de todas as strings do conjunto

    Parâmetros:
    Conjunto(set) --conjunto de strings
    """
    lista_do_conjunto = list(conjunto)
    prefixo = ""
    maior_prefixo_possivel = lista_do_conjunto[0]
    for caractere in maior_prefixo_possivel:
        for string in lista_do_conjunto:
            if not string.startswith(prefixo + caractere):
                return prefixo
        prefixo += caractere
    return prefixo

