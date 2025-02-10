#Faça uma função que, dadas duas listas l1 e l2, nos diz se l1 é
#menor ou igual (lexicograficamente) a l2

def eh_menor_ou_igual_lexicograficamente(l1,l2):
    if len(l1) <= len(l2):
        for i in range(len(l1)):
            if l1[i] == l2[i]:
                continue
            elif l1[i] > l2[i]:
                return False
            else:
                return True
        #Se os caracteres de l1 forem iguais (l1 é igual a l2 ou sufixo próprio de l2)
        return True
    else:
        for i in range(len(l2)):
            if l1[i] == l2[i]:
                continue
            elif l1[i] > l2[i]:
                return False
            else:
                return True
        #Aqui, l2 é sufixo próprio de l1
        return False
    




