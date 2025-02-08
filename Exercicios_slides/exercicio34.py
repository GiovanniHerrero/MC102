#a) Faça uma função "mapeia" que, dada uma lista l e uma função
#de um parâmetro f, devolve uma nova lista onde f foi aplicada
#a cada elemento de l.
#Por exemplo, se l = [1, 2, 3] e f(x) = x * x, então a nova
#lista é [1, 4, 9].

#b) Use a função que você criou para, dada uma lista, encontrar
#uma nova lista com todos os seus elementos elevado ao
#quadrado.

#Resolvendo o item a:
def mapeia(l, funcao):
    nova_lista = list()
    for i in l:
        novo_elemento = funcao(i)
        nova_lista.append(novo_elemento)
    return nova_lista

#Resolvendo o item b:
def eleva_ao_quadrado(x):
    return x*x

n = int(input("Digite quantos elementos sua lista terá"))
lista = list()
for i in range(n):
    novo_numero = float(input("Digite o próximo elemento da lista"))
    lista.append(novo_numero)

lista = mapeia(lista,eleva_ao_quadrado)
print(lista)
    