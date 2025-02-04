#(a) Dado n, imprima todos os números ímpares menores do que n.
#Obs: assumimos que a entrada é sempre maior ou igual do que zero

n = int(input())

if n % 2 == 0:
    n = n-1
else:
    n = n-2

while(n>0):
    print(n)
    n = n-2
    