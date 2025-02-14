#Faça uma função que, dados conjuntos s1 e s2, devolve um
#novo conjunto representando a interseção de s1 e s2

def intersecao(s1,s2):
    """Returns the intersection of two given sets
    
    Paramethers:
    s1 -- one set
    s2 -- the other set
    """
    s3 = set()
    for i in s1:
        if i in s2:
            s3.add(i)
    return s3