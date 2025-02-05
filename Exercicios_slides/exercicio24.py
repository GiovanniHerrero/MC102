n = int(input("Entre com a quantidade de números: "))
lista = list()

for i in range(n):
    numero = int(input("Digite o próximo número: "))
    lista.append(numero)

for i in range(n):
    if i == 0:
        if lista[i]<lista[i+1]:
            print(i)
    
    elif i == n - 1:
        if lista[i-1]<lista[i-2]:
            print(n-1)
    
    else:
        if lista[i-1]>lista[i] and lista[i]<lista[i+1]:
            print(i)
