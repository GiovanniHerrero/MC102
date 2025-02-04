#Um número é perfeito se é igual a soma dos seus divisores próprios (ex:
#6 = 1 + 2 + 3). Faça um programa que dado um número n,
#imprime todos os números perfeitos menores ou iguais a n.


#Função para verificar se um número é perfeito
def eh_perfeito(x):
    soma = 0
    for i in range(1, (x//2) + 1):
        if x%i == 0:
            soma = soma + i 
    
    if x == soma and x!= 0:
        return True
    else:
        return False
    

#Leitura da entrada e impressão da saída:
n = int(input("Entre com n: "))

for i in range(n+1):
    if eh_perfeito(i):
        print(i)

    
