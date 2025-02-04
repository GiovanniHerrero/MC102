#Leia uma sequência de números e imprima o menor

n = int(input("Digite a quantidade de números na sequência: "))
menor = float(input("Digite o primeiro número"))

for i in range(n-1):
    proximo = float(input("Digite o próximo número: "))
    if proximo < menor:
        menor = proximo
print(f"O menor número é: {menor}.")