#Leia uma sequência de números e verifique se todos são pares

n = int(input("Digite a quantidade de números na sequência: "))

todos_pares = True
i = 0

while(todos_pares and i<n):
    proximo = float(input("Digite o próximo número da sequência: "))
    i = i + 1
    if proximo % 2 == 1:
        todos_pares = False

if todos_pares:
    print("Todos são pares")
else:
    print("Nem todos são pares")
        