#a) Faça uma função combina que permite aplicar uma função f
#sobre uma lista l para combinar os seus resultados e obter um
#único valor.
# Ex: Podemos somar todos os elementos de uma lista de
#números.
# Ex: Podemos multiplicar todos os elementos de uma lista de
#números.
# Ex: Podemos fazer and de vários valores booleanos.
#b) Use a função que você criou para concatenar a representação
#decimal de uma lista de números inteiros positivos.
# Ex: se a lista é [1, 2, 0, 15], o resultado é ’12015’

#Resolvendo o item a:
def combina(l, funcao):
    valor_final = l[0]
    for i in l:
        if i is valor_final:
            continue
        else:
            valor_final = funcao(valor_final,i)
    return valor_final

#Resolvendo o item b:
def concatena(x,y):
    return str(x) + str(y)

#Lendo a entrada e imprimindo a saída:
n = int(input("Digite o número de elementos que sua lista terá: "))
lista = list()
for i in range(n):
    numero = int(input("Digite o próximo elemento da sua lista: "))
    lista.append(numero)
print(combina(lista, concatena))



