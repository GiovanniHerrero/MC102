#Faça um programa que, dada uma lista de nomes
#de alunos, imprima um histograma para tais nomes (utilizando um dicionário)


n = int(input("Entre com a quantidade de nomes que você irá digitar: "))
dicionario = dict()
for i in range(n):
    nome = input("Digite o nome do(a) aluno(a): ")
    if nome in dicionario:
        dicionario[nome]+=1
    else:
        dicionario[nome] = 1

for chave, valor in dicionario.items():
    print(f"{chave}: "+ dicionario[chave]*"*")


