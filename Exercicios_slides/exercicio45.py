#Faça um programa, que dado uma lista de número inteiros em
#[0, 10), imprime um histograma para tais números (utilizando dicionários):
 
#Construção e preenchimento do dicionário
n = int(input("Entre a quantidade de números que irá digitar: "))
dicionario = dict()
for i in range(n):
    numero = int(input())
    if numero in dicionario:
        dicionario[numero]+=1
    else:
        dicionario[numero] = 1

#Impressão da saída
for chave,valor in dicionario.items():
    print(f"{chave}: " + valor*"*" + "\n")