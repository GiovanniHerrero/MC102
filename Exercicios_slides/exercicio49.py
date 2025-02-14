#Faça uma função que, dados conjuntos s1 e s2, devolve um
#novo conjunto representando a união de s1 e s2

def uniao(s1,s2):
    """Returns the union of two sets
    
    Paramethers:

    s1 -- one set
    s2 -- another set
    """
    s3 = set()

    for element in s1:
        s3.add(element)
    for element in s2:
        s3.add(element)
    return s3