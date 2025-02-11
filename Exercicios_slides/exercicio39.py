#Faça uma função que, dadas duas strings s e t, verifica se s é
#substring de t.

def eh_substring(s,t):
    """Retorna um booleano indicando se s é substring de t

    Parâmetros:

    s --string que desejamos verificar ser substring
    t -- string de comparação
    """
    l_s = len(s)
    l_t = len(t)
    if l_s > l_t:
        return False
    else: 
        for i in range(l_t - l_s + 1):
            j = 0
            substring = True
            while(substring and j < l_s):
                if s[j] == t[i+j]:
                    j+=1
                else:
                    substring = False
            
            if substring:
                return True
        return False
    
print(eh_substring("abc","abxabyabc"))