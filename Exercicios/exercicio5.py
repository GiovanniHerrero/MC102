#Programa que lê dois números inteiros
#x e y e diz em qual quadrante do plano
#o ponto (x,y) está.

x = int(input("Digite a abcissa do ponto: "))
y = int(input("Digite a ordenada do ponto: "))

if y > 0:
    if x > 0:
        print(f"O ponto ({x},{y}) está no primeiro quadrante")
    elif x< 0:
        print(f"O ponto ({x},{y}) está no segundo quadrante")
    else:
        print(f"O ponto ({x},{y}) está no eixo das ordenadas")

elif y < 0:
    if x > 0:
        print(f"O ponto ({x},{y}) está no quarto quadrante")
    elif x < 0:
        print(f"O ponto ({x},{y}) está no terceiro quadrante")
    else:
        print(f"O ponto ({x},{y}) está no eixo das ordenadas")

else:
    if x == 0:
        print(f"O ponto ({x},{y}) está na origem")
    else:
        print(f"O ponto ({x},{y}) está no eixo das abcissas")

