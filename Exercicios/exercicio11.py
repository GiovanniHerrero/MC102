#Leia uma sequência de números e imprima a soma

n = int(input("Digite a quantidade de números na sequência: "))

soma = 0
for i in range(n):
    numero = float(input("Digite um número: "))
    soma +=numero

print(f"A soma é {soma}")