#Faça um histograma para nomes de alunos:


#Leitura dos nomes, criação e preenchimento das estruturas
n = int(input("Entre a quantidade de nomes que irá digitar:"))

lista_nomes = list()
lista_frequencia = list()


for i in range(n):
    nome = input()
    if nome in lista_nomes:
        lista_frequencia[lista_nomes.index(nome)]+=1
    else:
        lista_nomes.append(nome)
        lista_frequencia.append(1)

#Impressão da saída
print()
for i in range(len(lista_nomes)):
    print(f"{lista_nomes[i]}: ", end="")
    print(lista_frequencia[i]*"*")