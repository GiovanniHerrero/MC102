#Leia uma sequência de números e conte quantos são pares

n = int(input("Digite a quantidade de números na sequência: "))
pares = 0
for i in range(n):
    numero = float(input("Digite o próximo número da sequência: "))
    if numero % 2 == 0:
        pares = pares + 1

print(f"Há {pares} números pares na sequência dada")