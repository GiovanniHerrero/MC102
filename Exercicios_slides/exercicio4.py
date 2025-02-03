#Programa que lê dois números x e y, sendo
#y monodígito na base 10 e verifica se y é
#o último dígito (na base 10) de x.

x = int(input("Digite x"))
y = int(input("Digite y"))

if (x % 10) == y:
    print("Verdadeiro")
else:
    print("Falso")