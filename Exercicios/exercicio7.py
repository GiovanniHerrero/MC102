#Programa para calcular as raízes de uma
#equação do segundo grau a^x² + bx + c = 0

def le_termo_dominante():
    a = int(input("Digite o coeficiente do termo quadrático: "))

    while(a == 0):
        a = int(input("O coeficiente dominante não pode ser nulo. Entre outro coeficiente: "))
    
    return a


negativo = True

while(negativo):
    a = le_termo_dominante()
    b = int(input("Digite o coeficiente do termo 'x': "))
    c = int(input("Digite o termo independente: "))

    deltha = b**2 - 4*a*c
    
    if deltha < 0:
        print("Discriminante negativo. Entre outros valores para a, b e c")
    else:
        negativo = False

x_1 = ((-b + deltha**(1/2))/2*a)
x_2 = ((-b - deltha**(1/2))/2*a)

print(f"As raízes são {x_1} e {x_2}")
    


