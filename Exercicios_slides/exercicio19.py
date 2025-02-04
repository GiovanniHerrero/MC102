#Dado um inteiro n seguido por n inteiros, imprima o menor
#valor e o maior valor dos n inteiros, seguido pela quantidade
#de vezes que esses valores se repetem.

n = int(input("Entre com n:"))

#Lemos o primeiro número. Nesse momento, ele é o maior e o menor número simultanemante, e sua frequência é unitária
numero = int(input("Entre com o número: "))
menor = numero
maior = numero

frequencia_menor = 1
frequencia_maior = 1

#Loop principal
for i in range(n-1):
    numero = int(input("Entre com o número: "))

    if numero < menor:
        menor = numero
        frequencia_menor = 1

    elif numero == menor:
        frequencia_menor = frequencia_menor + 1

    elif numero > maior:
        maior = numero
        frequencia_maior = 1
    
    elif numero == maior:
        frequencia_maior = frequencia_maior + 1

print(f"Menor valor: {menor}. Frequência: {frequencia_menor}")
print(f"Maior valor: {maior}. Frequência: {frequencia_maior}")
