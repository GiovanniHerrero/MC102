#Escreva um programa que lê três números e encontra o maior
#dos três.

a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
c = float(input("Digite um terceiro número: "))

if a>= b:
    if c>= a:
        print(c)
    else:
        print(a)
elif c>= b:
    print(c)
else:
    print(b)
