#Faça uma função que dados dois conjuntos, retorna um conjunto
#contendo qualquer valor que pode ser obtido como soma de um elemento
#do primeiro com um elemento do segundo.

def soma_cartesiana(conjunto1,conjunto2):
    """Dados dois conjuntos, retorna um terceiro conjunto formado por elementos
    c t.q c = a + b com "a" pertencente a conjunto1 e "b" pertencente a conjunto2
    
    Parâmetros:
    conjunto1 (set) -- o conjunto dos elementos "a"
    conjunto2 (set) -- o conjunto dos elementos "b"

    Retorno:
    conjunto3(set)
    """
    conjunto3 = set()
    for elemento1 in conjunto1:
        for elemento2 in conjunto2:
            conjunto3.add(elemento1 + elemento2)
    return conjunto3

