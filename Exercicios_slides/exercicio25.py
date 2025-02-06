#Faça uma função que devolve a lista dos divisores de um
#número

def divisores(x):
    divisores = list()
    for i in range(1,x):
        if x%i == 0:
            divisores.append(i)
    return divisores

