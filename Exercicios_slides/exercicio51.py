#Faça uma função que, dados conjuntos s1 e s2, devolve um
#novo conjunto representando a subtração de s2 em s1:

def subtraction(s1,s2):
    """Returns the set given by the subtraction of s2 from s1
    
    Paramethers:
    s1 --the original set from which elements will be subtracted
    s2 -- the set whose elements will be subtracted
    """
    s3 = set()
    for element in s1:
        if element not in s2:
            s3.add(element)
    return s3