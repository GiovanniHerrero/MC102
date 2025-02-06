#Um número é triangular se ele é igual ao produto de três inteiros
#consecutivos.
#Faça uma função que, dado um número n, decide se ele é
#triangular ou não

def eh_trinagular(x):
    if x < 6:
        return False
    elif x == 6:
        return True
    else:
        for i in range(1,x//2):
            if i*(i+1)*(i+2) == x:
                return True
        return False
    
=


            
