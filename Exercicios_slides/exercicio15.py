#Dado um número, imprima a sua decomposição em números primos:

n = int(input("Digite um número: "))

k = 2
while (n != 1):
    if n % k == 0:
        print(k)
        n = n/k
    else:
        k = k + 1