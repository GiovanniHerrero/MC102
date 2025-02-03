n = int(input())
print(n)

notas_100 = n // 100
print(f"{notas_100} nota(s) de R$ 100,00")
n = n - notas_100*100

notas_50 = n//50
print(f"{notas_50} nota(s) de R$ 50,00")
n = n - notas_50*50

notas_20 = n//20
print(f"{notas_20} nota(s) de R$ 20,00")
n = n - notas_20*20

notas_10 = n//10
print(f"{notas_10} nota(s) de R$ 10,00")
n = n - notas_10*10

notas_5 = n//5
print(f"{notas_5} nota(s) de R$ 5,00")
n = n - notas_5*5

notas_2 = n//2
print(f"{notas_2} nota(s) de R$ 2,00")
n = n - notas_2*2

notas_1 = n
print(f"{notas_1} nota(s) de R$ 1,00")

