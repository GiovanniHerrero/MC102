#Programa que, dada uma lista de números, testa se todos são primos

#Função para verificar se um número é primo
def eh_primo(x):
    k = 2
    primo = True
    while(primo and k**2<=x):
        if x%k == 0:
            primo = False
        k+=1
    return (primo and x>=2)

#Função para verificar se todos os números em uma lista são primos
def todos_primos(lista):
    for i in lista:
        if not eh_primo(i):
            return False
    return True

#Leitura da entrada e impressão da saída
n = int(input("Digite quantos números sua lista terá: "))
lista = list()

for i in range(n):
    numero = int(input("Digite o próximo número da sua lista: "))
    lista.append(numero)

if todos_primos(lista):
    print("Todos os números da lista são primos.")
else:
    print("Nem todos os números da lista são primos.")

