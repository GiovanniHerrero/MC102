#Leia uma sequência de números e imprima o menor

n = int(input("Digite a quantidade de números na sequência: "))
menor = 0

for i in range(n):
    proximo = float(input("Digite o próximo número: "))
    if proximo < menor:
        menor = proximo
print(f"O menor número é: {menor}.")