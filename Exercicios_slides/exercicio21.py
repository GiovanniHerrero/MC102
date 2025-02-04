#Faça um programa que conta quantos primos menores do que
#n existem
def eh_primo(x):
    k = 2
    primo = True
    while(primo and k**2<=x):
        if x%k == 0:
            primo = False
        k+=1
    return (primo and x>=2)

def numero_primos_menores(x):
    total = 0
    for i in range(2,x):
        if eh_primo(i):
            total+=1
    return total

n = int(input("Entre com um número natural: "))

print(f"Há {numero_primos_menores(n)} números primos menores do que {n}")
