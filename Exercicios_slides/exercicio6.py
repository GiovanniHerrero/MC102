#O tempo Unix nos diz quantos segundos se passaram desde a
#Época Unix (00:00 de 01 de Janeiro de 1970 — UTC).

#Escreva um programa que dado um tempo Unix diz qual é o dia da
#semana daquele tempo

#Obs: 01/01/1970 foi um quinta-feira

tempo_unix = int(input("Digite o tempo Unix: "))


#Cálculo da quantidade de dias passados
dias_passados = (tempo_unix/3600)/24

#Cálculo do dia da semana:
dia_da_semana = dias_passados % 7

print("O dia da semana é: " , end="")

if dia_da_semana < 1:
    print("Quinta-Feira")

elif dia_da_semana < 2:
    print("Sexta-Feira")

elif dia_da_semana < 3:
    print("Sábado")

elif dia_da_semana < 4:
    print("Domingo")

elif dia_da_semana < 5:
    print("Segunda-Feira")

elif dia_da_semana < 6:
    print("Terça-Feira")
    
else:
    print("Quarta-Feira")