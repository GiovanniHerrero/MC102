#Escreva um programa que lê dois números inteiros x e y e diz
#qual quadrante do espaço (x, y) está, utilizando
#operadores lógicos

x = int(input("Digite a abcissa do ponto: "))
y = int(input("Digite a ordenada do ponto: "))

if x > 0 and y > 0:
    print("Primeiro quadrante")
elif x < 0 and y > 0:
    print("Segundo quadrante")
elif x < 0 and y < 0:
    print("Terceiro Quadrante")
elif x > 0 and y < 0:
    print("Quarto Quadrante")

else:
    print("As coordenadas digitadas correspondem a um ponto que está em um dos eixos ou na origem")