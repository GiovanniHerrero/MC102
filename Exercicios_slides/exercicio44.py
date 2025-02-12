#Faça um programa que permita buscar o RA de um aluno a
#partir do seu nome. (utilizando dicionários)

n = int(input("Digite quantos alunos você deseja adicionar ao dicinário: "))
dicionario = dict()
for i in range(n):
    nome, ra = input().split()
    ra = int(ra)
    dicionario[nome] = ra

m = int(input("Digite quantos RA's você deseja buscar no dicionário: "))
for i in range(m):
    nome = input()
    print(f"nome: {nome} RA: {dicionario[nome]}")