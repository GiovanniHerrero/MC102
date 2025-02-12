#Leia uma quantidade n de pares de nome/RA de alunos. Faça
#um programa que permita buscar o RA de um aluno a partir
#do seu nome.

#Função que busca um ra a partir de um nome
def busca_ra(nome,lista_alunos,lista_ra):
    """Devolve o RA (registro acadêmico) a partir de um nome de um aluno
    
    Parâmetros:
    lista_alunos --lista com nomes de alunos
    lista_ra --lista com os RA's
    nome --o nome que desejamos buscar

    Observação: o RA na i-ésima posição de lista_ra corresponde ao nome na i-ésima posição de lista_alunos
    """
    k = 0
    while(lista_alunos[k] != nome):
        k+=1
    return lista_ra[k]

#Criação e preenchimento de lista_alunos e lista_ra
n = int(input("Entre com a quantidade de nomes de alunos: "))
lista_alunos = list()
lista_ra = list()

for i in range(n):
    nome , ra = input().split()
    ra = int(ra)
    
    lista_alunos.append(nome)
    lista_ra.append(ra)

#Leitura das consultas e impressão das saídas
m = int(input("Entre com a quantidade de consultas que deseja fazer: "))
for i in range(m):
    nome = input()
    print(f"Nome: {nome} RA: {busca_ra(nome,lista_alunos,lista_ra)}\n")
