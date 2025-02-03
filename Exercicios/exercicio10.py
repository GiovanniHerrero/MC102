#Dê um exemplo onde utilizar if x ... else é diferente de usar if
#x seguido de if not x.

#Usando if x ... else:

x = True

if x:
    print("X é verdadeiro")
    x = False
else:
    print("X é falso")

#Usando if x seguido de if not x:
x = True

if x:
    print("X é verdadeiro")
    x = False
if not x:
    print("X é falso")

#Comentário: Na segunda situação, como há verificação das duas condicionais (if e if not)
# e como modificamos o valor lógico de x em uma delas, ambas são verificadas e executadas, o que
# não ocorre na primeira abordagem.