
#Faça uma função que, dados conjuntos s1 e s2, devolve se s1
#é subconjunto de s2.

def is_subset(s1,s2):
    """Returns a boolean indicating if s1 is a subset of s2
    
    Paramethers:
    s1 --the set we want to know if is subset
    s2 --the superset to check against
    """
    for element in s1:
        if element not in s2:
            return False
    return True