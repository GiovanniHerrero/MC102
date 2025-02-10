#Faça uma função que, dadas duas strings s e t, verifica se s é
#prefixo de t:


def eh_prefixo(s,t):
    """Retorna um booleano indicando se "s" é prefixo de "t"

    Parâmetros:
    s -- A string que desejamos verificar ser prefixo de t
    t -- A string de comparação
    """
    if len(s) > len(t):
        return False
    else:
        n = len(s)
        prefixo = True
        i = 0
        while(prefixo and i < n):
            if s[i] == t[i]:
                i+=1
            else:
                prefixo = False

        return prefixo

