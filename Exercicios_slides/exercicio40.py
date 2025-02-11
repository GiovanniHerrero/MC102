#Faça uma função que, dada uma string s e uma string sep,
#devolve uma lista resultante da quebra de s em uma ou mais
#strings, em cada ocorrência de sep:

def separador(s,sep):
    lista = list()
    string =""
    for i in range(len(s)):
        if s[i] == sep:
            lista.append(string)
            string =""
        else:
            string+=s[i]
    #Adiciona a última string à lista
    lista.append(string)

    return lista

