#Faça uma função que recebe dois dicionários e retorna sua
#soma. Isto é um terceiro dicionário com os pares (chave-valor)
#dos primeiros, mas onde as chaves forem iguais, os valores são
#somados.


def soma_dicionarios(dicionario1, dicionario2):
    dicionario3 = dict()
    for chave, valor in dicionario1.items():
        dicionario3[chave] = valor

    for chave, valor in dicionario2.items():
        if chave in dicionario3:
            dicionario3[chave]+=valor
        else:
            dicionario3[chave] = valor
    return dicionario3

