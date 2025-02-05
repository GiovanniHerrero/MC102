#Este programa calcula o valor de um investimento com saldo inicial s
#após n meses com uma taxa de juros anual de j

#Não há depósitos ou retiradas do investimento
#A taxa de juros é dada em porcentagem sem o síbolo %
#O jutos é aplicado no final do mês


saldo_inicial = int(input("Qual o saldo inicial? "))
n_meses = int(input("Por quanto tempo (meses) fará a aplicação? "))
taxa_de_juros_anual = int(input("Qual a taxa de juros básica anual atualmente (em porcentagem)? "))

#Conversão de taxa anual para taxa mensal e cálculo do valor final

taxa_mensal = (1+taxa_de_juros_anual/100)**(1/12)-1
valor_investimento = saldo_inicial*(1+taxa_mensal)**(n_meses)

#Impressão da saída
print(f"O valor final do investimento é de R${valor_investimento:.2f}")