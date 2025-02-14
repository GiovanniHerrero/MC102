#Faça uma função que recebe um conjunto de inteiros S e um inteiro x e
#retorna um conjunto contendo todos os pares de valores de S que
#somados resultam em x

def funcao(S,x):
    
    conjunto = set()
    for elemento1 in S:
        for elemento2 in S:
            if elemento1 != elemento2 and elemento1 + elemento2 == x:
                conjunto.add({elemento1,elemento2})
    return conjunto
