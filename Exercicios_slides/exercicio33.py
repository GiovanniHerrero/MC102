#Use a função seleciona e a biblioteca math para criar uma função
#que dada uma lista de números reais, devolve uma lista dos
#números x tal que x em radianos está no primeiro quadrante

import math

def seleciona(lista, funcao):
    """
    Retorna uma lista com elementos de "lista" selecionados pela "função"

    Argumentos:
    lista -- A lista que terá seus elementos selecionados
    funcao -- A função que irá selecionar os elementos
    """
    nova_lista =[]
    for x in lista:
        if funcao(x):
            nova_lista.append(x)
        return nova_lista

def esta_primeiro_quadrante(x):
    """Verifica que um número não negativo x está no primeiro quadrante do ciclo trigonométrico

    Parâmetros:
    x -- número não negativo (em radianos)
    """
    b = (x%(math.pi*2))
    return b >= 0  and b < math.pi/2
    
