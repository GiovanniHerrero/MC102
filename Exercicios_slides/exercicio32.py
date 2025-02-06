#Faça uma função que, dados dois números inteiros m (por padrão
#valendo 1) e n (por padrão valendo 5), desenhe m triângulos
#invertidos na tela, cada um com base n, usando caracteres ’

def desenha_trinagulos_invertidos(m,n):
    """Desenha m triângulos invertidos, cada um com base n
    
    Parâmetros:
    m -- quantidade de triângulos invertidos
    n -- tamanho da base de cada triângulo
    """
    for i in range(m):
        recuo = 0
        b = n
        while(b>0):
            print(recuo * " ", end =" ")
            print(b*"* ")
            b -= 2
            recuo += 2
        print()

