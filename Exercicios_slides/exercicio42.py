#Faça um programa, que dado uma lista de número inteiros em
#[0, 10), imprime um histograma para tais números.

lista = [0]*10

n = int(input("Digite quantos números tera a sua lista: "))


for i in range(n):
    numero = int(input())
    lista[numero]+=1

for i in range(10):
    print(f"{i}: ", end ="")
    print(lista[i]*"*")

