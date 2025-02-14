#Faça uma função que dados dois conjuntos de números inteiros, retorna
#dois novos conjuntos: um com os dobros dos elementos repetidos e outro
#com a metade (inteira) dos elementos não repetidos.

def function(conjunto1, conjunto2):
    """
    Retorna dois conjuntos: um com os dobros dos elementos repetidos
    e outro com a metade (inteira) dos elementos não repetidos

    Parâmetros:
        conjunto1 (set): Primeiro conjunto de números inteiros
        conjunto2 (set): Segundo conjunto de números inteiros

    Retorna:
        tuple: Dois conjuntos: dobros de elementos repetidos e metades dos elementos não repetidos
    """

    conjunto_dos_dobros = set()
    conjunto_das_metades = set()

    #Encontra os elementos repetidos (na interseção) e adiciona seus dobros ao conjunto dos dobros
    for element in conjunto1 & conjunto2:
        conjunto_dos_dobros.add(2*element)

    #Encontra os elementos não repetidos e adiciona sua metade(inteira) ao conjunto das metades
    for element in conjunto1 ^ conjunto2:
        conjunto_das_metades.add(element // 2)

    return conjunto_dos_dobros, conjunto_das_metades
